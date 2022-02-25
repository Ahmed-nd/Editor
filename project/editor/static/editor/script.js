document.getElementById("file").onchange = function() {
    document.getElementById("form").submit();
};
var viewsType = document.getElementById("views_type")
viewsType.onchange = function() {
    var value = viewsType.value
    console.log(value)
    var display = document.getElementById("display")
    if (value == "original"){
        display.classList.add("view-orgin");
        display.classList.remove("view-full");
    }else if (value == "full"){
        display.classList.add("view-full");
        display.classList.remove("view-orgin");
    }
};