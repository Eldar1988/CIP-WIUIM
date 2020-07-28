function AjaxAddContact() {
  let post_url = $(".wpcf7-form").attr("action");
  // get token
  let csrf_token = $('.wpcf7-form [name="csrfmiddlewaretoken"]').val();
  // data for send
  let name = $("#name").val();
  let phone = $("#phone").val();
  let page_title = $("title").text();

  // give data
  let data = {};
  data["csrfmiddlewaretoken"] = csrf_token;
  data.name = name;
  data.phone = phone;
  data.title = page_title;
  data.url = window.location.href;

  let status = 0;
  if (name.length < 3) {
    $("#error-name").empty();
  } else {
    status += 1;
  }
  if (phone.length < 7) {
    $("#error-phone").empty();
  } else {
    status += 1;
  }

  if (status == 2) {
    $("#error-name").empty();
    $("#error-phone").empty();
    $("#error-text-id").empty();
    swal("Спасибо!", "Мы свяжемся с Вами в ближайшее время.", "success");
    $.ajax({
    url: post_url,
    type: "POST",
    data: data,
    success: () => {},
  });
  }
  if (status < 2) {
    swal(
      "Ошибка",
      "Все поля формы должны быть заполнены.",
      "warning"
    );
  }
}


function AjaxAddSubscribe() {
  console.log('start')
  let post_url = $(".mc4wp-form").attr("action");
  // get token
  let csrf_token = $('.mc4wp-form [name="csrfmiddlewaretoken"]').val();
  // data for send
  let email = $("#email-sub").val();
  console.log(email)

  // give data
  let data = {};
  data["csrfmiddlewaretoken"] = csrf_token;
  data.email = email;

  let status = 0;
  if (email.length < 5) {
    $("#error-email").empty();
    $("#error-email").append("Введите корректный email");
  } else {
    status += 1;
  }

  if (status == 1) {
    swal("Спасибо!", "Мы свяжемся с Вами в ближайшее время.", "success");
    $.ajax({
    url: post_url,
    type: "POST",
    data: data,
    success: () => {},
  });
  }
  if (status == 0) {
    swal(
      "Ошибка",
      "Все поля формы должны быть заполнены.",
      "warning"
    );
  }
}



