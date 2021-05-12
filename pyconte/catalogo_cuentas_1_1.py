from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

__NAMESPACE__ = "www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas"


class CatalogoMes(Enum):
    VALUE_01 = "01"
    VALUE_02 = "02"
    VALUE_03 = "03"
    VALUE_04 = "04"
    VALUE_05 = "05"
    VALUE_06 = "06"
    VALUE_07 = "07"
    VALUE_08 = "08"
    VALUE_09 = "09"
    VALUE_10 = "10"
    VALUE_11 = "11"
    VALUE_12 = "12"


@dataclass
class Catalogo:
    """
    Estándar de catálogo de cuentas que se entrega como parte de la
    contabilidad electrónica.

    :ivar ctas: Nodo obligatorio para expresar el detalle de cada cuenta
        y subcuenta del catálogo.
    :ivar version: Atributo requerido para expresar la versión del
        formato
    :ivar rfc: Atributo requerido para expresar el RFC del contribuyente
        que envía los datos
    :ivar mes: Atributo requerido para expresar el mes en que inicia la
        vigencia del catálogo para la balanza
    :ivar anio: Atributo requerido para expresar el año en que inicia la
        vigencia del catálogo para la balanza
    :ivar sello: Atributo opcional para contener el sello digital del
        archivo de contabilidad electrónica. El sello deberá ser
        expresado cómo una cadena de texto en formato Base 64
    :ivar no_certificado: Atributo opcional para expresar el número de
        serie del certificado de sello digital que ampara el archivo de
        contabilidad electrónica, de acuerdo al acuse correspondiente a
        20 posiciones otorgado por el sistema del SAT.
    :ivar certificado: Atributo opcional que sirve para expresar el
        certificado de sello digital que ampara al archivo de
        contabilidad electrónica como texto, en formato base 64.
    """
    class Meta:
        namespace = "www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas"
        namespace_prefix = "catalogocuentas"
        schema_location = "http://www.sat.gob.mx/esquemas/ContabilidadE/1_1/CatalogoCuentas/CatalogoCuentas_1_1.xsd"

    ctas: List["Catalogo.Ctas"] = field(
        default_factory=list,
        metadata={
            "name": "Ctas",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    version: str = field(
        init=False,
        default="1.1",
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
    rfc: Optional[str] = field(
        default=None,
        metadata={
            "name": "RFC",
            "type": "Attribute",
            "required": True,
            "min_length": 12,
            "max_length": 13,
            "pattern": r"[A-ZÑ&]{3,4}[0-9]{2}[0-1][0-9][0-3][0-9][A-Z0-9]?[A-Z0-9]?[0-9A-Z]?",
        }
    )
    mes: Optional[CatalogoMes] = field(
        default=None,
        metadata={
            "name": "Mes",
            "type": "Attribute",
            "required": True,
        }
    )
    anio: Optional[int] = field(
        default=None,
        metadata={
            "name": "Anio",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 2015,
            "max_inclusive": 2099,
        }
    )
    sello: Optional[str] = field(
        default=None,
        metadata={
            "name": "Sello",
            "type": "Attribute",
            "white_space": "collapse",
        }
    )
    no_certificado: Optional[str] = field(
        default=None,
        metadata={
            "name": "noCertificado",
            "type": "Attribute",
            "length": 20,
        }
    )
    certificado: Optional[str] = field(
        default=None,
        metadata={
            "name": "Certificado",
            "type": "Attribute",
            "white_space": "collapse",
        }
    )

    @dataclass
    class Ctas:
        """
        :ivar cod_agrup: Atributo requerido para expresar el código
            asociador de cuentas y subcuentas conforme al catálogo
            publicado en la página de internet del SAT. Se debe asociar
            cada cuenta y subcuenta que sea más apropiado de acuerdo con
            la naturaleza y preponderancia de la cuenta o subcuenta.
        :ivar num_cta: Atributo requerido, es la clave con que se
            distingue la cuenta o subcuenta en la contabilidad
        :ivar desc: Atributo requerido para expresar el nombre de la
            cuenta o subcuenta
        :ivar sub_cta_de: Atributo opcional en el caso de subcuentas.
            Sirve para expresar la clave de la cuenta a la que pertenece
            dicha subcuenta. Se convierte en requerido cuando se cuente
            con la información.
        :ivar nivel: Atributo requerido para expresar el nivel en el que
            se encuentra la cuenta o subcuenta en el catálogo.
        :ivar natur: Atributo requerido para expresar la naturaleza de
            la cuenta o subcuenta. (D - Deudora, A - Acreedora). (
            Activo = D ) ( Pasivo = A ) ( Capital = A ) ( Ingreso = A )
            ( Costo = D ) ( Gasto = D ) ( Resultado Integral de
            Financiamiento = D y/o A ) ( Cuentas de orden = D y/o A ).
        """
        cod_agrup: Optional[str] = field(
            default=None,
            metadata={
                "name": "CodAgrup",
                "type": "Attribute",
                "required": True,
            }
        )
        num_cta: Optional[str] = field(
            default=None,
            metadata={
                "name": "NumCta",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 100,
            }
        )
        desc: Optional[str] = field(
            default=None,
            metadata={
                "name": "Desc",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 400,
            }
        )
        sub_cta_de: Optional[str] = field(
            default=None,
            metadata={
                "name": "SubCtaDe",
                "type": "Attribute",
                "min_length": 1,
                "max_length": 100,
            }
        )
        nivel: Optional[int] = field(
            default=None,
            metadata={
                "name": "Nivel",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1,
            }
        )
        natur: Optional[str] = field(
            default=None,
            metadata={
                "name": "Natur",
                "type": "Attribute",
                "required": True,
                "pattern": r"[DA]",
            }
        )
