function MapReload() {
  ymaps.ready(init);
  function init() {
    let myMap = new ymaps.Map(
      "YMapsID",
      {
        center: [47.866831, 67.828261],
        zoom: 4,
      },
      {
        searchControlProvider: "yandex#search",
      }
    );

    $.ajax({
      url: "http://127.0.0.1:8000/give_map/",
      type: "GET",
      success: (data) => {
        let q = 0;
        for (let i in data) {
          let x = data[q].fields.x;
          let y = data[q].fields.y;
          let title = data[q].fields.map_title;
          let body = data[q].fields.short_description;
          let slug = data[q].fields.slug;
          q++;
          myMap.geoObjects.add(
            new ymaps.Placemark(
              [x, y],
              {
                balloonContent: `${body} <br><a href="https://cipwiuim.kz/map/object/${slug}" class="map-link">Подробнее</a>`,
                iconCaption: `${title}`,
              },
              {
                preset: "islands#icon",
                iconColor: "#00c3ff",
              }
            )
          );
        }
      },
    });
  }
}
MapReload();


async function MapSelfGenerate(x, y) {
    let newX = x.replace(',', '.')
    let newY = y.replace(',', '.')

    document.getElementById('SelfMap').style.height = '400px'
    $('#map-btn').fadeOut()
    $('#map-btn-hide').fadeIn()
    function sleep(ms) {
        return new Promise((resolve) => setTimeout(resolve, ms));
    }
    await sleep(1500);


    $('#map-btn-hide').click(function () {
        document.getElementById('SelfMap').style.height = '0px'
        // $('#SelfMap').fadeOut();
        // $('#map-btn-hide').fadeOut();
        // $('#map-btn').fadeIn()
        $('#MapDiv').fadeOut();


    })

    ymaps.ready(init);

    function init() {
        let myMap = new ymaps.Map(
            "SelfMap",
            {
                center: [newX, newY],
                zoom: 6,
            },
            {
                searchControlProvider: "yandex#search",
            }
        );
        myMap.geoObjects.add(
            new ymaps.Placemark(
                [newX, newY],
                {
                    balloonContent: '',
                    iconCaption: '',
                },
                {
                    preset: "islands#icon",
                    iconColor: "#00c3ff",
                }
            )
        );

    }
}