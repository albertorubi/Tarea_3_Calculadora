#!/usr/bin/env python
# coding: utf-8

# In[2]:


class CalculadoraBasica:

  
    def capturar_valores(self, a, b):
        self.a = a
        self.b = b

 
    def sumar(self):
        return self.a + self.b

  
    def restar(self):
        return self.a - self.b

 
    def multiplicar(self):
        return self.a * self.b

  
    def dividir(self):
        return self.a / self.b

if __name__ == "__main__":
    miCalculadora =CalculadoraBasica()

    
    resultado = 0

    print('--Calculadora básica--')
    operacion = input('Seleccione la función realizar \n '                        '+  - * /')
    valor1= input('Ingrese el primer número')
    valor1 = int(valor1)
    valor2 = input('Ingrese el segundo número')
    valor2 = int(valor2)

    
    miCalculadora.capturar_valores(valor1, valor2)

    if operacion == '+':
        resultado = miCalculadora.sumar()
    elif operacion == '-':
        resultado = miCalculadora.restar()
    elif operacion == '*':
        resultado = miCalculadora.multiplicar()
    elif operacion == '/':
        resultado = miCalculadora.dividir()
    else:
        pass
    print(f'El resultado de {operacion}',
          f' el número {valor1}',
          f' y el número {valor2}',
          f'es de {resultado}')


# In[ ]:




