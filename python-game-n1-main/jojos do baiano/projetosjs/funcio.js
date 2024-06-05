let func = ['João','Maria','camila','Ana','Pedro','Laura','Tiago','Mariana','Matheus','Sofia'];
    func.push('Mateus','Isabela','Rafael','Camila-Fernandes');
    func.splice(2,1);
    func.splice(4,1);
    func.push('Vitoria');
    func.push('ana');

console.log(func);

let funcs = [... new Set(func)]
console.log(funcs);