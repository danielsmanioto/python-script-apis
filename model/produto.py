import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Produto:

    def __init__(self, codigo: str, descricao: str):
        logger.info("Construtor iniciar")
        logger.info(f"id={codigo}, descricao={descricao}")

        self._codigo = codigo
        self._descricao = descricao

    @property
    def codigo(self) -> str:
        logger.info("Getter codigo chamado")
        return self._codigo

    @codigo.setter
    def codigo(self, value: str):
        logger.info(f"Setter codigo chamado com value={value}")
        self._codigo = value

    @property
    def descricao(self) -> str:
        logger.info("Getter descricao chamado")
        return self._descricao

    @descricao.setter
    def descricao(self, value: str):
        logger.info(f"Setter descricao chamado com value={value}")
        self._descricao = value

    def cadastrar(self):
        logger.info(f"Cadastrando produto: id={self.codigo}, descricao={self.descricao}")


for i in range(200):
    produto = Produto(codigo=i, descricao="Coca Cola")
    produto.cadastrar()
    logger.info(f"Produto cadastrado = {produto.codigo} e {produto.descricao}")
