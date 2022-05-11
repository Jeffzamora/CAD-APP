// funciopn del spiner loading
// $(window).on('load', function () {
//     setTimeout(function () {
//         $(".loader-page").css({visibility: "hidden", opacity: "0"})
//     }, 400);
//
// });


// segunda forma de hacer funcionar el spiner loading
$(window).load(function () {
    $(".loader-page").fadeOut("slow");
});

// Funcion del click derecho
// window.onload = function () {
//     document.addEventListener("contextmenu", function (e) {
//         e.preventDefault();
//     }, false);
// };