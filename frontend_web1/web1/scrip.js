     function validar(){
        cedula = parseInt(document.getElementById("ci").value);
        if (cedula <= 800000){
            alert(cedula)
            respuesta = confirm("Rango invalido. \n ¿Enviar de todos modos?");
            return respuesta;
        }
     }