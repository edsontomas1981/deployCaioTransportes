const romaneioExiste = ()=>{
    let romaneio = document.getElementById('numRomaneio')
    if (romaneio.textContent == ''){
        msgErro('Antes de continuar Selecione um Romaneio')
        return 
    }
    return romaneio.textContent
}

const excluiNf = async (element)=>{
    let numManifesto = document.getElementById('numRomaneio').textContent
    let resposta = await msgConfirmacao('Deseja remover a nota fiscal ?')
    if (resposta){
        let response  = await connEndpoint('/operacional/delete_nf_romaneio/', {'numManifesto':numManifesto,'idNumNf':element});
        let novosDados = prepara_dados_tbody(response.manifesto.nota_fiscal_fk)    
    }
}

const prepara_dados_tbody=(dados)=>{
    let botoes={
        alterar: {
            classe: "btn-primary text-white",
            texto: '<i class="fa fa-search" aria-hidden="true"></i>',
            callback: handlerNotaFiscal
          },
        excluir: {
            classe: "btn-danger text-white",
            texto: '<i class="fa fa-trash" aria-hidden="true"></i>',
            callback: excluiNf
          }
      };

    let dadosPreparados = []
    dados.forEach(element => {
        console.log(element)
        let statusHTML = getStatusLabel(element.status);
        dadosPreparados.push({id:element.id,numNf:element.num_nf,remetente:element.remetente.raz_soc,destinatario:element.destinatario.raz_soc,
            origem:element.remetente.endereco_fk.cidade,destino:element.destinatario.endereco_fk.cidade,peso:element.peso,valor:element.valor_nf,
            status:statusHTML
        })
    });
    popula_tbody_paginacao('navegacaoNfsRomaneio','romaneioNotas',dadosPreparados,botoes,1,50,false,false)            
    return dadosPreparados
}   

