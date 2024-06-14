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

document.getElementById('btnNumNf').addEventListener('click',async ()=>{
    let response = await connEndpoint('/operacional/updateNfStatusNf/', {'idNf':document.getElementById('idNumNf').value,
                                                                        'numNf':document.getElementById('cmbStatus').value,
    });
    populaPaginaNotasFiscais()
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



