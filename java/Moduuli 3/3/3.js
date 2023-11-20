const names = ['John', 'Paul', 'Jones'];
const target = document.getElementById('target');

let lista = "";
for (let i = 0; i < names.length; i++) {
    lista += "<li>" + names[i] + "</li>";
}
target.innerHTML = lista;
