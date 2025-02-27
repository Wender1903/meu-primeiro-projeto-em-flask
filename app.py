from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def exemplo():
    class Aluno:
        def __init__(self, nome, ap1, ap2, pai1, pai2, pai3, pf):
            self.nome = nome
            self.ap1 = ap1
            self.ap2 = ap2
            self.pai1 = pai1
            self.pai2 = pai2
            self.pai3 = pai3
            self.pf = pf
            self.maps = 0
            self.mpai = 0
            self.mf = 0

        def __str__(self):
            return f'{self.nome} \nMAPs: {self.maps} \nMPAI: {self.mpai} \nPF: {self.pf} \nMF: {self.mf}'

        def calcular_maps(self):
            self.maps = ((self.ap1 + self.ap2) / 2) 
            return self.maps
        
        def calcular_mpai(self):
            self.mpai = ((self.pai1 + self.pai2 + self.pai3) / 3) 
            return self.mpai
        
        def calcular_media_final(self):
            mpai = self.calcular_mpai() * 0.30
            maps = self.calcular_maps() * 0.30
            pf = self.pf * 0.40
            self.mf = maps + maps + pf
            return self.mf
        


    aluno1 = Aluno('Larissa Pires', 10, 10, 7, 7, 7, 8)
    maps = aluno1.calcular_maps()
    mpai = aluno1.calcular_mpai()
    mf = aluno1.calcular_media_final()

    aluno = {'Nome': aluno1.nome, 'MAPs': maps, 'MPAI': mpai, 'PF': aluno1.pf, 'MF': mf}

    

            
        

    
    return jsonify(aluno)

if __name__ == '__main__':
    app.run(debug=True)
