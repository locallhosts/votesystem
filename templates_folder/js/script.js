 const selectElement = document.querySelector("#poll-select");
  const submitBtn = document.querySelector("#submit-btn");

  selectElement.addEventListener("change", function() {
    if (selectElement.value === "Please Select Vote") {
      submitBtn.disabled = true;
    } else {
      submitBtn.disabled = false;
    }
  });