var app = new Vue({
  'el': '#app',
  'data': {
    menuList: [
      { 'name': 'Randevu', 'iconClass': 'fa-calendar' },
      { 'name': 'Randevu Listesi', 'iconClass': 'fa-list'},
      { 'name': 'Öğrenci Listesi', 'iconClass': 'fa-users' }
    ],
    selectedMenu: 'Randevu',
  },
  'methods': {
    logoffOnclick: function () {
      result = request('DELETE', '/api/auth', [], null);
      result = JSON.parse(result);
      if (result.status == 'OK') {
        location.reload();
      }
    }
  }


});
