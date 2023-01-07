// Получить модель
var modal = document.getElementById("myModal");

// Получите изображение и вставьте его внутрь модального - используйте его текст "alt" в качестве подписи
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

// Получить элемент <span>, который закрывает модальный
var span = document.getElementsByClassName("close")[0];

// Когда пользователь нажимает на <span> (x), закройте модальное окно
span.onclick = function() {
  modal.style.display = "none";
}


$(document).click(function (e) {
    if ($(e.target).is('.modal')) {
        closeModal();
    }
});