 import numpy as np
 import matplotlib.pyplot as plt
 from sklearn.linear_model import LinearRegression
 X = np.array([1, 2, 3, 4]).reshape(-1, 1)
 Y = np.array([3, 5, 6, 8])
 model = LinearRegression()
 model.fit(X, Y)
 a = model.coef_[0]
 b = model.intercept_
 print(f"Equação da reta: y = {a:.2f}x + {b:.2f}")
 x_valores = np.linspace(1, 4, 100).reshape(-1, 1)
 y_valores = model.predict(x_vals)
 plt.scatter(X, Y, color='green', label='Dados')
 plt.plot(x_valores, y_valores, color='red', label=f'Reta: y = {a:.2f}x +
 {b:.2f}')
 plt.xlabel('X')
 plt.ylabel('Y')
 plt.title('Regressão Linear')
 plt.legend()
plt.grid(True)
 plt.show()
