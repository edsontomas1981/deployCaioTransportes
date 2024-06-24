var responseNotaFiscal

const prepara_dados_nfs = (result)=>{
    let dados = []
    result.forEach(element => {
        const statusHTML = getStatusLabel(element.status);
        dados.push({
                    id:element.id,
                    nf:element.num_nf,
                    remetente:truncateString(element.remetente.raz_soc,15),
                    destinatario: element.destinatario.raz_soc ? truncateString(element.destinatario.raz_soc, 15) : 'N/A',
                    origem:truncateString(element.remetente.endereco_fk.bairro,7),
                    destino:truncateString(element.destinatario.endereco_fk.bairro,7),
                    volume:element.volume,
                    peso:element.peso,
                    valorNfe:element.valor_nf,  
                    status:statusHTML
                })
        });
    return dados
}


const criaOcorrencias = async () => {

    // Obtenha os dados dos elementos do DOM
    let idNf = document.getElementById('idNumNf').value;
    let ocorrencia_fk = document.getElementById('ocorrencia_fk').value;
    let nota_fiscal_fk = document.getElementById('nota_fiscal_fk').value;
    let observacao = document.getElementById('txtObservacao').value;
    let data = document.getElementById('txtDataOcorrencia').value;
    let imagemInput = document.getElementById('imagem');

    // Crie um FormData para enviar os dados e a imagem
    let formData = new FormData();
    formData.append('idNf', idNf);
    formData.append('ocorrencia_fk', ocorrencia_fk);
    formData.append('nota_fiscal_fk', ocorrencia_fk);
    formData.append('observacao', observacao);
    formData.append('data', data);
    
    if (imagemInput.files.length > 0) {
        formData.append('imagem', imagemInput.files[0]);
    }


    let camposObrigatorios = ['txtDataOcorrencia','ocorrencia_fk']
    let campos = obterDadosDoFormulario('formModalNf',camposObrigatorios)
    
    if (campos){
        // Envie os dados e a imagem
        let response = await fetch('/operacional/add_ocorrencia/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken') // Assumindo que você está usando CSRF em seu Django
            },
            body: formData
        });
        
        if (response.ok) {
            let result = await response.json();
            console.log(result);
            populaPaginaNotasFiscais();
        } else {
            console.error('Erro ao atualizar a ocorrência');
        }
    }
};

// Função auxiliar para obter o CSRF token do cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function changeImage(newSrc) {
    // Obtém o elemento img pelo ID
    const imgElement = document.getElementById('imgEvidencia');

    // Altera o atributo src para a nova URL da imagem
    imgElement.src = newSrc;
}

document.getElementById('btnNumNf').addEventListener('click',async ()=>{
        criaOcorrencias()
})

document.addEventListener('DOMContentLoaded',async ()=>{
    populaPaginaNotasFiscais()
})

const populaPaginaNotasFiscais = async()=>{
    let botoes = {
        mostrar: {
            classe: "btn-success text-white",
            texto: '<i class="fa fa-window-restore" aria-hidden="true"></i>',
            callback: handlerNotaFiscal
        },
        excluir: {
            classe: "btn-danger text-white",
            texto: '<i class="fa fa-print" aria-hidden="true"></i>',
            callback: get_notas_selecionadas
        }
    };

    let response = await connEndpoint('/operacional/readNfs/', {});
    let dadosTbody = response.nfs
    let dadosParametrizados = prepara_dados_nfs(dadosTbody)
    popula_tbody_paginacao('paginacaoTodasNfs','relatorioNfs',dadosParametrizados,botoes,1,20,true,false)

}





