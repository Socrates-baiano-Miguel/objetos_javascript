let dinheiroshow = 100
let idade = 18;

if(dinheiroshow >= 150 && idade >= 18)
{
    console.log ('voce pode entrar no show');
}

else if (dinheiroshow < 150 && idade >= 18) {
    console.log('voce não tem dinheiro o suficiente')
}

else if (dinheiroshow >= 150 && idade < 18) {
    console.log('voce não tem idade o suficiente')
}

else {
    console.log('voce não tem dinheiro e idade para entrar')
}


