app.controller('myProductCtrl', function ($scope, $http, $window, $rootScope) {
    $scope.products = [];
    $scope.mama = $rootScope.url;
    $scope.sellerId = $window.sellerId;
    $scope.productId = $window.productId;
    var transactionTypeUsage = 2;
    var amount = 10;


    $scope.getId = function (id) {
        $scope.sellerId = id;
        getProduct();
    };


    var getProduct = function() {
        // debugger;
        $http.get($scope.mama + '/api/products/?seller_id=' + $scope.sellerId).then(
            function (response) {
                $scope.products = response.data.results;
            },
            function (response) {
                console.log(response)
            })
    }

    $scope.delProduct = function (productId) {
        $http.delete($scope.mama + '/api/products/' + productId).then(
            function (response) {
                $scope.products = response;
                alert('delete success!!')
                getProduct();
            }
        )
    };

    $scope.promoteProduct = function (){
        var data = {
            account : $scope.sellerId,
            transaction_type : transactionTypeUsage,
            amount : amount,
            promoted_product : $scope.productId
        };


        $http.post($scope.mama + '/api/coin_transactions/', data).then(
            function success(response) {
                alert('สินค้าชิ้นนี้ถูกโปรโมทแล้ว')
            },
            function () {
                alert('fail')
            }

        )
    };


});