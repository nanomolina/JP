angular
  .module('patient')
  .controller('patientCtrl', patientCtrl);

function patientCtrl() {
  var vm = this;

  vm.listPacients = [];
  vm.getPatients = getPatients;

  function getPatients() {
    
  }
}
