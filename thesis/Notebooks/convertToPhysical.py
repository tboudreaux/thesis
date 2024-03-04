from readCPython import load_C_output
from getXi1 import find_root

import numpy as np
import argparse

G = 6.674e-8 #cm^3 g^-1 s^-2
mp = 1.67e-24 # grams
k = 1.3807e-16 #cm^2 g s^-2 K^-1
L_solar = 3.839e33 # erg s^-1
sigma = 5.6704e-5 # erg cm^-2 s^-1 K^-4


def get_central_density(M, R, xi1, dthetaXdxi1):
    """ Find the centeral density

    Positional Arguments:
        M -> Stellar Mass in g
        R -> Stellar Radius in cm
        xi1 -> xi value of surface
        dthetaXdxi1 -> value of derivitive of theta at surface
    Returns:
        central density of star in cgs
    """
    return -(M*xi1)/(4*np.pi*R**3)*(1/dthetaXdxi1)

def get_density(M, R, xi1, theta, dthetaXdxi1, n):
    """ Find run of density with theta

    Positional Arguments:
        M -> Stellar Mass in g
        R -> Stellar Radius in cm
        xi1 -> xi value of surface
        theta -> solution to theta from integration
        dthetaXdxi1 -> value of derivitive of theta at surface
        n -> polytropic index
    Returns:
        density of star in cgs
    """
    return get_central_density(M, R, xi1, dthetaXdxi1)*np.power(theta, n)

def get_alpha(R, xi1):
    """ Find radius scale factor alpha

    Positional Arguments:
        R -> Stellar Radius in cm
        xi1 -> xi value of surface
    Returns:
        Alpha scale factor such that R = alpha * xi
    """
    return R/xi1


def get_radius(R, xi, xi1):
    """ Find radius scale factor alpha

    Positional Arguments:
        R -> Stellar Radius in cm
        xi -> dimensionless radius
        xi1 -> xi value of surface
    Returns:
        return r based on an xi
    """
    return xi*get_alpha(R, xi1)


def get_K(M, R, xi, theta, dthetaXdxi, xi1, dthetaXdxi1, n):
    """ The proportionality constant for the polytropic equation of state

    Positional Arguments:
        M -> Stellar Mass in g
        R -> Stellar Radius in cm
        xi -> dimensionless radius
        theta -> solution to theta from integration
        xi1 -> xi value of surface
        dthetaXdxi1 -> value of derivitive of theta at surface
        n -> polytropic index
    Returns:
        cgs proportionality constant
    """
    central_density = get_central_density(M, R, xi1, dthetaXdxi1)
    numerator = M**(2/3)*2**(2/3)*np.pi**(1/3)*G
    denominator = xi1**(4/3)*(n+1)*central_density**((3-n)/(3*n))
    return (numerator/denominator)*(-dthetaXdxi1)**(-2/3)


def get_P(M, R, xi, theta, dthetaXdxi, xi1, dthetaXdxi1, n):
    """ The Run of pressure with xi along the star

    Positional Arguments:
        M -> Stellar Mass in g
        R -> Stellar Radius in cm
        xi -> dimensionless radius
        theta -> solution to theta from integration
        xi1 -> xi value of surface
        dthetaXdxi1 -> value of derivitive of theta at surface
        n -> polytropic index
    Returns:
        Pressure run in the star in cgs
    """
    K = get_K(M, R, xi, theta, dthetaXdxi, xi1, dthetaXdxi1, n)

    return K*(get_central_density(M, R, xi1, dthetaXdxi1)**(1+1/n))*theta**(n+1)


def get_T(M, R, xi, theta, dthetaXdxi, xi1, dthetaXdxi1, n, mu):
    """ The Run of temperature with xi along the star

    Positional Arguments:
        M -> Stellar Mass in g
        R -> Stellar Radius in cm
        xi -> dimensionless radius
        theta -> solution to theta from integration
        xi1 -> xi value of surface
        dthetaXdxi1 -> value of derivitive of theta at surface
        n -> polytropic index
        mu -> mean molecular weight
    Returns:
        Temperature run in the star in cgs
    """
    return (get_P(M, R, xi, theta, dthetaXdxi, xi1, dthetaXdxi1, n)*mu*mp)/(k*get_density(M, R, xi1, theta, dthetaXdxi1, n))


def get_mu(X, Y, Z):
    """ Find the mean molecular weight

    Positional Arguments:
        X -> Hydrogen Abundence
        Y -> Helium Abundence
        Z -> Metallicity
    Returns:
        The mean molecular weight
    """

    return (1/(2*X+(3/4)*Y+(1/2)*Z))

def get_radius_from_luminosity_teff(LogL, Teff):
    """ Use the stephan boltzman law to get the radius from luminosity and temperature

    Positional Arguments:
        LogL -> log10(L/Lsolar)
        Teff -> Effective Temperature [Kelvin]
    Returns:
        Radius in cgs units

    """
    L = L_solar*10**LogL
    return (1/(2*Teff**2))*np.sqrt(L/(np.pi*sigma))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert the dimensionless values to physical values")
    parser.add_argument('path', metavar='<path/to/file>', type=str, help='Path to the binary dump')

    parser.add_argument('-m', '--mass', type=float, help="Stellar Mass")
    parser.add_argument('-r', '--radius',  type=float, help="Stellar Radius")
    parser.add_argument('-l', '--loglumin', type=float, help="log luminosity in solar luminosity units")
    parser.add_argument('-t', '--teff', type=float, help="Effective Temperature")

    parser.add_argument("-X", type=float, help="Hydrogen Abundence", default=0.76)
    parser.add_argument("-Y", type=float, help="Helium Abundence", default=0.24)
    parser.add_argument("-Z", type=float, help="Meltallicity", default=0)

    parser.add_argument("-o", "--output", type=str, help="Output Location", default="NULL")

    args = parser.parse_args()

    # Exctract the polytropic index from the file name convention
    n = float(args.path.split('/')[-1].split('_')[1][:-7])

    # Load data from the c dump binary
    state, metadata = load_C_output(args.path)
    xi1, thetaXi1 = find_root(state[0], state[1])
    dthetaXdxi1, _ = find_root(state[2], state[1])

    # Select only the portion of the the solution less than the radius of the star
    conditional = state[0] <= xi1

    xi = state[0][conditional]
    theta = state[1][conditional]
    dtheta = state[2][conditional]

    M = args.mass

    # Select a-priori radius or given luminosity and temperature
    if args.radius:
        R = args.radius
    else:
        assert args.loglumin and args.teff
        R = get_radius_from_luminosity_teff(args.loglumin, args.teff)

    radius = get_radius(R, xi, xi1)
    mu = get_mu(args.X, args.Y, args.Z)

    # Scale quantities to physical
    rho = get_density(M, R, xi1, theta, dthetaXdxi1, n)
    P = get_P(M, R, xi, theta, dtheta, xi1, dthetaXdxi1, n)
    T = get_T(M, R, xi, theta, dtheta, xi1, dthetaXdxi1, n, mu)

    # If output target is not given write to standard output
    if args.output == "NULL":
        print("xi,theta,dtheta,radius,rho,P,T")
        for x, t, dt, r, rh, p, t in zip(xi, theta, dtheta, radius, rho, P, T):
            print("{},{},{},{},{},{},{}".format(x, t, dt, r, rh, p, t))
    else:
        with open(args.output, 'wb') as f:
            output = np.array([xi, theta, dtheta, radius, rho, P, T])
            np.save(f, output)
