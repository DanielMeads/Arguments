# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting_template='Hello, <name>!'):
    greet_list = greeting_template.replace('<','{')
    greet_list = greet_list.replace('>', '}')
    greet = eval("f'{}'".format(greet_list))
    return greet

def force(mass, body="earth"):
    body_g = {
        "sun":274,
        "jupiter":24.9,
        "neptune":11.2,
        "saturn":10.4,
        "earth":9.8,
        "uranus":8.9,
        "venus":8.9,
        "mars":3.7,
        "mercury":3.7,
        "moon":1.6,
        "pluto":.6
    }
    force = (float(mass)) * (body_g[body])
    return force

def pull(m1, m2, d):
    G = 6.674e-11
    pull = G*((float(m1))*(float(m2))/((float(d))**2))
    return pull

if __name__ == "__main__":
    name = "Daniel"
    greeting_template = 'OI OI, <name>!'

print (pull(800, 1500, 3))