 import numpy as np
 import matplotlib.pyplot as plt
 from sklearn.linear_model import LinearRegression
 x = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
 y = np.array([0, 2, 4, 5, 5])
 model = LinearRegression()
 model.fit(x, y)
 a = model.coef_[0]
 b = model.intercept_
 x_valores = np.linspace(1, 5, 100).reshape(-1, 1)
 y_valores = model.predict(x_valores)
 plt.scatter(x, y, color='green', label='Pontos Fornecidos')
 plt.plot(x_valores, y_valores, color='red', label=f'Reta: y = {b:.2f} +
 {a:.2f}x')
 plt.xlabel('x')
 plt.ylabel('y')
 plt.title('Regressão Linear')
 plt.legend()
 plt.grid(True)
 plt.show()
