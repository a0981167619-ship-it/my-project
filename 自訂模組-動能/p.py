def kinetic_energy(mass,velocity):
    mass=int(input('請輸入物體的質量:'))
    velocity=int(input('請輸入物體的速度:'))
    return 0.5*mass*velocity**2
def potential_energy(mass,height):
    mass=int(input('請輸入物體的質量:'))
    height=int(input('請輸入物體的高度'))
    return mass*9.8*height
