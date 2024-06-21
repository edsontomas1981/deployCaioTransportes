const romaneioExiste = ()=>{
    let romaneio = document.getElementById('numRomaneio')
    if (romaneio.textContent == ''){
        msgErro('Antes de continuar Selecione um Romaneio')
        return 
    }
    return romaneio.textContent
}

const prepara_dados_tbody=(dados)=>{
    let botoes={
        alterar: {
            classe: "btn-primary text-white",
            texto: '<i class="fa fa-search" aria-hidden="true"></i>',
            // callback: mostrarTabela
          },
        excluir: {
            classe: "btn-danger text-white",
            texto: '<i class="fa fa-trash" aria-hidden="true"></i>',
            // callback: excluirTabelas
          }
      };
    let dadosPreparados = []
    dados.forEach(element => {
        let statusHTML = getStatusLabel(element.status);
        dadosPreparados.push({id:element.id,numNf:element.num_nf,remetente:element.remetente.raz_soc,destinatario:element.destinatario.raz_soc,
            origem:element.remetente.endereco_fk.cidade,destino:element.destinatario.endereco_fk.cidade,peso:element.peso,valor:element.valor_nf,
            status:statusHTML
        })
    });
    popula_tbody_paginacao('navegacaoNfsRomaneio','romaneioNotas',dadosPreparados,botoes,1,50,false,false)            
    return dadosPreparados
}   

