function addComment(name, id) {
  document.getElementById("parent").value = id;
  document.getElementById("comment").innerText = `${name.bold()}, `;
}

async function AjaxDelComment(id) {
  let comment_url = $("#delComm").attr("href");
  console.log(comment_url);
  let csrf_token = $('.comment-form [name="csrfmiddlewaretoken"]').val();
  let data = {};
  data.id = id;
  data["csrfmiddlewaretoken"] = csrf_token;
  $.ajax({
    url: comment_url,
    type: "POST",
    data: data,
    success: () => {},
  });
  swal("Отлично!", "Комментарий удален.", "success");
  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  await sleep(2000);
  $.ajax({
    type: "GET",
    success: (data) => {
      $("#comments").empty();
      $("#comments").append($(data).find("#comments").html());

      $(".comment-counter").empty();
      $(".comment-counter").append($(data).find(".comment-counter").html());
    },
  });
}

async function AjaxAddComment() {
  let post_url = $(".comment-form").attr("action");
  // get token
  let csrf_token = $('.comment-form [name="csrfmiddlewaretoken"]').val();
  // data for send
  let name = $("#name").val();
  let email = $("#email").val();
  let text = $("#comment").val();
  let parent = $("#parent").val();
  let page_title = $(".entry-title").text();

  let status = 0;
  if (name.length < 3) {
    $("#error-name").empty();
    $("#error-name").append("Как к Вам обращаться?");
  } else {
    status += 1;
  }
  if (email.length < 7) {
    $("#error-email").empty();
    $("#error-email").append(
      "Пожалуйста, оставьте Вашу почту. Она не будет опубликована."
    );
  } else {
    status += 1;
  }
  if (text.length < 1) {
    $("#error-text-id").empty();
    $("#error-text-id").append("Нелья оставлять пустой комментарий.");
  } else {
    status += 1;
  }
  if (status == 3) {
    $("#error-name").empty();
    $("#error-email").empty();
    $("#error-text-id").empty();
    swal("Отлично!", "Ваш комментарий опубликован.", "success");
  }
  if (status == 0) {
    swal(
      "Ошибка",
      "Все поля формы комментария должны быть заполнены.",
      "warning"
    );
  }
  // give data
  let data = {};
  data["csrfmiddlewaretoken"] = csrf_token;
  data.name = name;
  data.email = email;
  data.text = text;
  data.parent = parent;
  data.title = page_title;
  data.url = window.location.href;

  $.ajax({
    url: post_url,
    type: "POST",
    data: data,
    success: () => {},
  });

  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
  await sleep(3000);

  $.ajax({
    type: "GET",
    success: (data) => {
      $(".comment-form-comment").empty();
      $(".comment-form-comment").append(
        $(data).find(".comment-form-comment").html()
      );

      $("#comments").empty();
      $("#comments").append($(data).find("#comments").html());

      $(".comment-counter").empty();
      $(".comment-counter").append($(data).find(".comment-counter").html());
    },
  });
}
