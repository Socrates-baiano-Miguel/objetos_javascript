let client = {
    name: "Miguel",
    age: 18,
    cpf: "989804937294873",
    email: "migs@example.com",
    phone: ["(43)666666666", "40028922"],
};
client.address = [{
    road:"Vereador Domingos Lourenço",
    Number:"12",
    apartment:"not",
    complement:"perto da APAE",
}];
client.address.push({
    street:false,
    apartment:true,
    comlement:false,
    number:666,
});

client.address.pop();
 
    for(let chave in client){
        console.log(chave)
    }