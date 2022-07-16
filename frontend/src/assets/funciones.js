

export function dateFormat (fecha) {
    var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', hour12: false};
    let fcha = new Date(fecha)
    let convertida = fcha.toLocaleDateString('es-ES', options);
    return convertida;
}

export function primeraLetra (texto) {
    return texto.charAt(0).toUpperCase();
}
