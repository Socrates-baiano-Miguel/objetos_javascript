
let objectpessoal = {
    nome: "Miguel",
    idade: 18,
    cpf: "989804937294873",
    email: "migs@example.com",

}
 console.log(`Nome do Felizardo é ${objectpessoal.nome} e a idade do caboco é de ${objectpessoal.idade} anos e os s 3 primeiros números do cpf ${objectpessoal.cpf.substring(12,15)} `) 

 let keys  = ['nome', 'idade', 'cpf', 'email']

 keys.forEach ((key) => {
    console.log(`Nome do Felizardo é ${objectpessoal["nome"]} e a idade do caboco é de ${objectpessoal["idade"]}`) 
 } 

);

