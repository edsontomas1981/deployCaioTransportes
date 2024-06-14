const getStatusLabel = (status) => {
    switch (status) {
        case 1:
            return '<label class="badge badge-success">Entregue</label>'; //Processo Finalizado com Sucesso
        case 2:
            return '<label class="badge badge-danger">Cancelado</label>';//Processo Cancelado
        case 3:
            return '<label class="badge badge-secondary">Pendente</label>';//Processo pendente por falta de documentação,pagamentos etc. 
        case 4:
            return '<label class="badge badge-info">Em Progresso</label>';//Nf Alocada em veiculo para fazer a entrega
        case 5:
            return '<label class="badge badge-warning">Em Espera</label>';// Aguadando no Armazem status inicial
        default:
            return '<label class="badge badge-primary">Outros</label>';
    }
};

const prepara_dados_nfs = (result)=>{
    let dados = []
    result.forEach(element => {
        const statusHTML = getStatusLabel(element.status);
        dados.push({
                    id:element.id,
                    nf:element.num_nf,
                    remetente:truncateString(element.remetente.raz_soc,15),
                    destinatario:truncateString(element.destinatario.raz_soc,15),
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
    // let ocorrencia_fk = document.getElementById('ocorrencia_fk').value;
    // let nota_fiscal_fk = document.getElementById('nota_fiscal_fk').value;
    // let observacao = document.getElementById('observacao').value;
    // let data = document.getElementById('data').value;
    // let criado_por = document.getElementById('criado_por').value;
    // let atualizado_por = document.getElementById('atualizado_por').value;
    let imagemInput = document.getElementById('imagem');

    // Crie um FormData para enviar os dados e a imagem
    let formData = new FormData();
    formData.append('idNf', idNf);
    // formData.append('ocorrencia_fk', ocorrencia_fk);
    // formData.append('nota_fiscal_fk', nota_fiscal_fk);
    // formData.append('observacao', observacao);
    // formData.append('data', data);
    // formData.append('criado_por', criado_por);
    // formData.append('atualizado_por', atualizado_por);
    
    if (imagemInput.files.length > 0) {
        formData.append('imagem', imagemInput.files[0]);
    }

    console.log(formData);
    
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

    

document.getElementById('btnNumNf').addEventListener('click',async ()=>{
        criaOcorrencias()

        // Crie um objeto FormData
        // let formData = [];
        // formData.push({'idNf':document.getElementById('idNumNf').value,
        //     'numNf': document.getElementById('cmbStatus').value});
    
        // Adicione outros campos necessários
        // formData.append('ocorrencia_fk', document.getElementById('ocorrencia_fk').value);
        // formData.append('nota_fiscal_fk', document.getElementById('nota_fiscal_fk').value);
        // formData.append('observacao', document.getElementById('observacao').value);
        // formData.append('data', document.getElementById('data').value);
        // formData.append('criado_por', document.getElementById('criado_por').value);
        // formData.append('atualizado_por', document.getElementById('atualizado_por').value);
        
        // console.log(formData)
        // // Adicione o arquivo de imagem
        // let imagemInput = document.getElementById('imagem');
        // if (imagemInput.files.length > 0) {
        //     formData.push({'imagem': imagemInput.files[0]});
        // }
        
        // console.log(formData)

        // let response = await connEndpoint('/operacional/updateNfStatusNf/', {'dados':formData});
        // populaPaginaNotasFiscais()    
        

        // // Faça a requisição
        // let response = await fetch('/operacional/updateNfStatusNf/', {
        //     method: 'POST',
        //     body: formData,
        //     headers: {
        //         'X-CSRFToken': getCookie('csrftoken') // Assumindo que você está usando CSRF em seu Django
        //     }
        // });
    
        // if (response.ok) {
        //     let result = await response.json();
        //     console.log(result);
        //     populaPaginaNotasFiscais();
        // } else {
        //     console.error('Erro ao atualizar a ocorrência');
        // }
})

const handlerNotaFiscal = async(element)=>{
    let responseNotaFiscal = await connEndpoint('/operacional/readNfId/', {'idNf':element});
    openModal('modalAlteraNotas')
    document.getElementById('txtIdNumNf').value=responseNotaFiscal.nota_fiscal.num_nf
    document.getElementById('txtModalRemetente').value=responseNotaFiscal.nota_fiscal.remetente.raz_soc
    document.getElementById('txtModalDestinatario').value=responseNotaFiscal.nota_fiscal.destinatario.raz_soc

    document.getElementById('idNumNf').value=element

    let response = await connEndpoint('/operacional/ocorrenciasNfs/', {});
    let dadosSelect = []

    console.log(response)
    
    response.tipos.forEach(dado =>{
        dadosSelect.push({value:dado.id,text:dado.ocorrencia})
    })
    select = new SelectHandler()
    select.populaSelect('cmbStatus',dadosSelect)
}

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
          //   callback: enviarMensagemWebSocket
        }
    };

    let response = await connEndpoint('/operacional/readNfs/', {});
    let dadosTbody = response.nfs
    let dadosParametrizados = prepara_dados_nfs(dadosTbody)
    popula_tbody_paginacao('paginacaoTodasNfs','relatorioNfs',dadosParametrizados,botoes,1,20,false,false)
}



