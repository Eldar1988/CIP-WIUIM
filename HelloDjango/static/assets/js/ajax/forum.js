function addCommentForum(name, id) {
  console.log(id, name);
  document.getElementById("answer_for").value = id;
  CKEDITOR.instances.id_text.setData(`${name}, `);
}

async function AjaxAddCommentForum(redirect_url) {
  // request.POST url
  let post_url = $(".comment-form").attr("action");
  // get token
  let csrf_token = $('.comment-form [name="csrfmiddlewaretoken"]').val();
  // data for send
  let name = $("#name").val();
  let email = $("#email").val();
  let answer_for = $("#answer_for").val();
  let text = CKEDITOR.instances.id_text.getData();
  let title = $("h4").text()

  let status = 0;
  if (name.length < 2) {
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
  if (text.length < 2) {
    $("#error-text-id").empty();
    $("#error-text-id").append("Нелья оставлять пустой комментарий.");
  } else {
    status += 1;
  }

  if (status == 3) {
    $("#error-name").empty();
    $("#error-email").empty();
    $("#error-text-id").empty();
    swal({
      title: "Отлично",
      text: "Ваше сообщение опубликовано. Спасибо за проявленный интерес!",
      icon: "success",
      buttons: ["Проверить", "Остаться тут"],
      dangerMode: true,
    }).then((willDelete) => {
      if (willDelete) {
        CKEDITOR.instances.id_text.setData("");
      } else {
        document.location.href = `${redirect_url}#theme-comment-start`;
      }
    });
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
  data.answer_for = answer_for;
  data.title = title;
  data.url = window.location.href;

  $.ajax({
    url: post_url,
    type: "POST",
    data: data,
    success: () => {
      $("textarea").empty();
    },
  });

  function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
  await sleep(3000);

  $.ajax({
    type: "GET",
    success: (data) => {
      $(".forum-answers-reload").empty();
      $(".forum-answers-reload").append(
          $(data).find(".forum-answers-reload").html()
      );
    },
  });
}

function AjaxReload() {
  $.ajax({
    type: "GET",
    success: (data) => {
      $(".forum-answers-reload").empty();
      $(".forum-answers-reload").append(
          $(data).find(".forum-answers-reload").html()
      );
    },
  });
}


async function AjaxDelForumComment(id) {
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
      $(".forum-answers-reload").empty();
      $(".forum-answers-reload").append(
          $(data).find(".forum-answers-reload").html()
      );
    },
  });
}
