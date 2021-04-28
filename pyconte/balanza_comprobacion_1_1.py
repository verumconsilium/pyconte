from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion"


class BalanzaMes(Enum):
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
    VALUE_13 = "13"


@dataclass
class Balanza:
    """
    Estándar de balanza de comprobación que se entrega como parte de la
    contabilidad electrónica.

    :ivar ctas: Nodo obligatorio para expresar el detalle de cada cuenta
        o subcuenta de la balanza de comprobación.
    :ivar version: Atributo requerido para expresar la versión del
        formato.
    :ivar rfc: Atributo requerido para expresar el RFC del contribuyente
        que envía los datos
    :ivar mes: Atributo requerido para expresar el mes al que
        corresponde la balanza de comprobación
    :ivar anio: Atributo requerido para expresar el año al que
        corresponde la balanza
    :ivar tipo_envio: Atributo requerido para expresar el tipo de envío
        de la balanza (N - Normal; C - Complementaria)
    :ivar fecha_mod_bal: Atributo opcional para expresar la fecha de la
        última modificación contable de la balanza de comprobación. Es
        requerido cuando el atributo TipoEnvio = C. Se convierte en
        requerido cuando se cuente con la información.
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
        namespace = "www.sat.gob.mx/esquemas/ContabilidadE/1_1/BalanzaComprobacion"

    ctas: List["Balanza.Ctas"] = field(
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
            "white_space": "collapse",
            "pattern": r"[A-ZÑ&]{3,4}[0-9]{2}[0-1][0-9][0-3][0-9][A-Z0-9]?[A-Z0-9]?[0-9A-Z]?",
        }
    )
    mes: Optional[BalanzaMes] = field(
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
    tipo_envio: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoEnvio",
            "type": "Attribute",
            "required": True,
            "pattern": r"[NC]",
        }
    )
    fecha_mod_bal: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "FechaModBal",
            "type": "Attribute",
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
        :ivar num_cta: Atributo requerido para expresar la clave
            asignada con que se distingue la cuenta o subcuenta en el
            catálogo de cuentas del  contribuyente.
        :ivar saldo_ini: Atributo requerido para expresar el monto del
            saldo inicial de la cuenta o subcuenta en el periodo. De
            acuerdo a la naturaleza de la cuenta o subcuenta, deberá de
            corresponder el saldo inicial, de lo contrario se entenderá
            que es un saldo inicial de naturaleza inversa. En caso de no
            existir dato, colocar cero (0)
        :ivar debe: Atributo requerido para expresar el monto de los
            movimientos deudores de la cuenta o subcuenta. En caso de no
            existir dato, colocar cero (0)
        :ivar haber: Atributo requerido para expresar el monto de los
            movimientos acreedores de la cuenta o subcuenta. En caso de
            no existir dato, colocar cero (0)
        :ivar saldo_fin: Atributo requerido para expresar el monto del
            saldo final de la cuenta o subcuenta en el periodo. De
            acuerdo a la naturaleza de la cuenta o subcuenta, deberá de
            corresponder el saldo final, de lo contrario se entenderá
            que es un saldo final de naturaleza inversa. En caso de no
            existir dato, colocar cero (0)
        """
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
        saldo_ini: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "SaldoIni",
                "type": "Attribute",
                "required": True,
                "min_exclusive": Decimal("-99999999999999.99"),
                "max_inclusive": Decimal("99999999999999.99"),
                "fraction_digits": 2,
                "white_space": "collapse",
            }
        )
        debe: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Debe",
                "type": "Attribute",
                "required": True,
                "min_exclusive": Decimal("-99999999999999.99"),
                "max_inclusive": Decimal("99999999999999.99"),
                "fraction_digits": 2,
                "white_space": "collapse",
            }
        )
        haber: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "Haber",
                "type": "Attribute",
                "required": True,
                "min_exclusive": Decimal("-99999999999999.99"),
                "max_inclusive": Decimal("99999999999999.99"),
                "fraction_digits": 2,
                "white_space": "collapse",
            }
        )
        saldo_fin: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "SaldoFin",
                "type": "Attribute",
                "required": True,
                "min_exclusive": Decimal("-99999999999999.99"),
                "max_inclusive": Decimal("99999999999999.99"),
                "fraction_digits": 2,
                "white_space": "collapse",
            }
        )
