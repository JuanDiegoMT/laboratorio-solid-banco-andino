class GeneradorExtractos:

    def generar(self, productos):
        for producto in productos:
            print(
                producto.generar_extracto()
            )