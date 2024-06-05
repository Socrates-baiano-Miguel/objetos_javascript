let funcionarios = ["Aline", "Ana Clara", "Camilly","Diego","Evellyn","Gabriel","Heloa","João Paulo", "João-Victor","José-Gabriel","Julia","Leonardo","Luana","Lucas","Maria Eduarda","Maria-Rafaela","Maria-Yasmim","Miguel","Rafael","Thauane"]
//mostrando todos os funcionários na tela
console.log(funcionarios)

//removendo o último elemento
let func = funcionarios.pop()
console.log(funcionarios)
console.log('###############################')
//removendo o primeiro elemento
let funcionar = funcionarios.shift()
console.log(funcionarios)
console.log('###############################')
//removendo por índice (a partir do indice , quantos quero remover)
let remover = funcionarios.splice(2,1);
console.log(funcionarios);
//remova o funcionário João Paulo
let jpdemitido = funcionarios.splice(7,1)
console.log(funcionarios)