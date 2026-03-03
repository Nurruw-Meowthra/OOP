"""Testisin siin Split meetodit, et saada filmi pealkiri ja aasta eraldi välja. Ja siis panin need kokku uue stringina, kus on pealkiri ja aasta koos."""


txt = "No Country For Old Men (2005)"

x = txt.split("(", 1)[0].strip()

y = txt.split("(", 1)[1].rstrip(")").strip()

z = f"{x} {int(y)}"

print(x)
print(y)
print(z)