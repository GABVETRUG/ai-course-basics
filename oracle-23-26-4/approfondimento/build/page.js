document.querySelectorAll(".copy").forEach(function (btn) {
  btn.addEventListener("click", function () {
    var code = btn.closest(".code").querySelector("code");
    var text = code.textContent;
    var reset = function () { setTimeout(function () { btn.textContent = "Copia"; }, 1600); };
    var selectText = function () {
      var range = document.createRange();
      range.selectNodeContents(code);
      var sel = window.getSelection();
      sel.removeAllRanges();
      sel.addRange(range);
      btn.textContent = "Selezionato";
      reset();
    };
    try {
      navigator.clipboard.writeText(text).then(function () {
        btn.textContent = "Copiato";
        reset();
      }, selectText);
    } catch (e) {
      selectText();
    }
  });
});
