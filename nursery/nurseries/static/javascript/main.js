if (localStorage.getItem("total") === null) {
    localStorage.setItem("total",0);

    var cart = {}
    
    localStorage.setItem("cart", JSON.stringify(cart));             
}

else {
    var exist = JSON.parse(localStorage['cart']);

    Object.keys(exist).forEach(function(key) {
        if (exist.hasOwnProperty(key)) {
            $("." + key).html(exist[key]);
        }   
        else {
            exist[key] = 0;
            localStorage.setItem("cart", JSON.stringify(exist));
        }
    });

    $(".cart_number").html(localStorage.total);

    console.log(localStorage);
}

function minus(id) {
    var exist = localStorage['cart'];
    exist = JSON.parse(exist);
    exist[id] = exist[id] - 1;
    localStorage.setItem("cart", JSON.stringify(exist));

    //total logic
    localStorage.total = parseInt(localStorage.total) - 1;

    exist = JSON.parse(localStorage['cart']);

    $('.'+id).html(exist[id]);
    $(".cart_number").html(localStorage.total);
    console.log(localStorage);
}

function plus(id) {
    //Cart Logic
    var exist = localStorage['cart'];
    exist = JSON.parse(exist);

    if(!exist.hasOwnProperty(id)) {
        console.log('nahi')
        exist[id] = 0;
        localStorage.setItem("cart", JSON.stringify(exist));
    }

    exist[id] = exist[id] + 1;
    localStorage.setItem("cart", JSON.stringify(exist));

    //total logic
    localStorage.total = parseInt(localStorage.total) + 1;

    exist = JSON.parse(localStorage['cart']);

    $('.'+id).html(exist[id]);
    $(".cart_number").html(localStorage.total);
    console.log(localStorage);
}

$('.send_data').click(function(event){
    console.log("Ajax Call")

    var exist = localStorage['cart'];
    exist = JSON.parse(exist);

    console.log(exist);

    $.ajax({
            data  : JSON.stringify({'plant_data' : exist}),
            type : 'POST',
            url : '/show_cart',
            processData: false,
            contentType: 'application/json; charset=utf-8'
    })
    .done(function(data) {
       console.log('SUCSESS !!', data.url);
       window.location.href = data.url;
    });
});
