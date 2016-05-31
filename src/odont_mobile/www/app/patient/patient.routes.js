angular
  .module('patient')
  .config(routes);

function routes($stateProvider, $urlRouterProvider) {
  $stateProvider

  .state('app.patient', {
      url: '/patient/list',
      views: {
        'menuContent': {
          templateUrl: 'app/patient/list.html',
          controller: 'patientCtrl'
        }
      }
    })
}
