'use strict';

angular.module('app')

.factory('RegrasDescontoService', function($http, $cookies, ApiService){
	return {

		loadRegrasDesconto(id){
		    var token = $cookies.get('token');
		    var req = {
		       method: 'GET',
		       url: ApiService.host + '/empresa/regras_desconto',
		       headers: {
		         'Authorization': 'Token ' + token
		       },
		    }

		    return $http(req)
		    .then((res) => {
		        return res
		    })
		    .catch((res) => {
		        return res
		    });
		},

		loadContratos(){
		    var token = $cookies.get('token');
		    var req = {
		       method: 'GET',
		       url: ApiService.host + '/contrato/',
		       headers: {
		         'Authorization': 'Token ' + token
		       },
		    }

		    return $http(req)
		    .then((res) => {
		        return res
		    })
		    .catch((res) => {
		        return res
		    });
		},

		criarPromocao(nova_promocao){
		    var token = $cookies.get('token');
		    var req = {
		       method: 'POST',
		       data:nova_promocao,
		       url: ApiService.host + '/desconto/',
		       headers: {
		         'Authorization': 'Token ' + token
		       },
		    }

		    return $http(req)
		    .then((res) => {
		        return res
		    })
		    .catch((res) => {
		        return res
		    });
		},

		editarPromocao(promocao){
		    var token = $cookies.get('token');
		    var req = {
		       method: 'PUT',
		       data:promocao,
		       url: ApiService.host + '/desconto/' + promocao.id + "/",
		       headers: {
		         'Authorization': 'Token ' + token
		       },
		    }

		    return $http(req)
		    .then((res) => {
		        return res
		    })
		    .catch((res) => {
		        return res
		    });
		},

		removerPromocao(promocao_id){
		    var token = $cookies.get('token');
		    var req = {
		       method: 'DELETE',
		       url: ApiService.host + '/desconto/'+promocao_id + "/",
		       headers: {
		         'Authorization': 'Token ' + token
		       },
		    }

		    return $http(req)
		    .then((res) => {
		        return res
		    })
		    .catch((res) => {
		        return res
		    });
		},




	};
});
