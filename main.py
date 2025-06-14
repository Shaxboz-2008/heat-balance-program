def calc_kerosene_mass(m=5, t1=-50, t3=100, eta=0.8):
    c_ice = 2100          # Дж/(кг·°C)
    lambda_melt = 3.3e5   # Дж/кг
    c_water = 4200        # Дж/(кг·°C)
    q_kerosene = 4.6e7    # Дж/кг

    Q1 = c_ice * m * (0 - t1)
    Q2 = lambda_melt * m
    Q3 = c_water * m * (t3 - 0)
    Q_total = Q1 + Q2 + Q3

    Q_fuel = Q_total / eta
    return Q_fuel / q_kerosene

if __name__ == "__main__":
    mass = calc_kerosene_mass()
    print(f"Потребуется керосина: {mass:.4f} кг")
