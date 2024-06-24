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

const getStatusLabel = (status) => {
    switch (status) {
        case 1:
          return '<label class="badge badge-warning">Em Espera</label>';// Aguadando no Armazem status inicial
        case 'Em Espera':
            return '<label class="badge badge-warning">Em Espera</label>';// Aguadando no Armazem status inicial  
        case 2:
          return '<label class="badge badge-info">Em Progresso</label>';//Nf Alocada em veiculo para fazer a entregareturn '<label class="badge badge-success">Entregue</label>'; //Processo Finalizado com Sucesso    
        case 'Em Progresso':
          return '<label class="badge badge-info">Em Progresso</label>';//Nf Alocada em veiculo para fazer a entrega
        case 3:
            return '<label class="badge badge-secondary">Pendente</label>';//Processo pendente por falta de documentação,pagamentos etc. 
        case 'Pendente':
          return '<label class="badge badge-secondary">Pendente</label>';//Processo pendente por falta de documentação,pagamentos etc. 
        case 4:
          return '<label class="badge badge-success">Entregue</label>'; //Processo Finalizado com Sucesso    
        case 'Entregue':
          return '<label class="badge badge-success">Entregue</label>'; //Processo Finalizado com Sucesso    
        case 5:
          return '<label class="badge badge-danger">Cancelado</label>';//Processo Cancelado
        case 'Cancelado':
          return '<label class="badge badge-danger">Cancelado</label>';//Processo Cancelado
    
        default:
            return '<label class="badge badge-primary">Outros</label>';
    }
  };
  
  const get_notas_selecionadas = ()=>{
    console.log(getSelectedRows())
  }
  
  function getSelectedRows() {
    const selectedRows = [];
    const checkboxes = document.querySelectorAll('#relatorioNfs input[type="checkbox"]:checked');
  
    checkboxes.forEach(checkbox => {
        const row = checkbox.closest('tr');
        const rowData = {
            id:row.getAttribute('data-id'),
        };
        selectedRows.push(rowData);
    });
  
    return selectedRows;
  }
  
  const prepara_dados_ocorrencias = (dados)=>{
    let listaDados = []
    dados.forEach(e => {
        let statusHTML = getStatusLabel(e.ocorrencia.id);
        listaDados.push({
                           id:e.id, 
                           data:formataData(e.data),
                           ocorrencia:e.ocorrencia.tipo_ocorrencia,
                           usuario:e.criado_por,
                           status:statusHTML,
        })
    });
    return listaDados
  }
  
  function changeImageById(recordId) {
    // Encontra o registro correspondente ao ID
    const record = responseNotaFiscal.ocorrencias.find(record => record.id === recordId);
    // Verifica se o registro foi encontrado
    if (record) {
        // Altera a imagem do elemento img
        document.getElementById('imgEvidencia').src = record.imagem_path;
    } else {
        alert('Registro não encontrado');
    }
  }
  
  const modalEvidencia = (element)=>{
    openModal('modalEvidencia')
    changeImageById(element)
  }
  
  const carrega_dados_ocorrencias = async()=>{
    let botoes = {
        mostrar: {
            classe: "btn-info text-white",
            texto: '<i class="fa fa-window-restore" aria-hidden="true"></i>',
            callback: modalEvidencia
        },
    }
    let idNotaFiscal = document.getElementById('idNumNf')
    responseNotaFiscal = await connEndpoint('/operacional/ocorrenciasNfs/', {'idNumNf':idNotaFiscal.value});
    let dadosOcorrencias = prepara_dados_ocorrencias(responseNotaFiscal.ocorrencias)
    popula_tbody_paginacao('paginacaoEventosNotas','eventosNotas',dadosOcorrencias,botoes,1,30,false,false)
  
  }
  
  const handlerNotaFiscal = async(element)=>{
    let responseNotaFiscal = await connEndpoint('/operacional/readNfId/', {'idNf':element});
    openModal('modalAlteraNotas')
    document.getElementById('nota_fiscal_fk').value=responseNotaFiscal.nota_fiscal.num_nf
    document.getElementById('txtModalRemetente').value=responseNotaFiscal.nota_fiscal.remetente.raz_soc
    document.getElementById('txtModalDestinatario').value=responseNotaFiscal.nota_fiscal.destinatario.raz_soc
  
    document.getElementById('idNumNf').value=element
  
    let response = await connEndpoint('/operacional/getAllTipoOcorrencia/', {});
    let dadosSelect = []
  
    console.log(response)
  
    carrega_dados_ocorrencias()
  
    response.ocorrencias.forEach(dado =>{
        dadosSelect.push({value:dado.id,text:dado.ocorrencia})
    })
    select = new SelectHandler()
    select.populaSelect('ocorrencia_fk',dadosSelect)
    get_notas_selecionadas()
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





