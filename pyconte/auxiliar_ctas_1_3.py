from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas"


@dataclass
class AuxiliarCtas:
    """
    Estándar de auxiliar de la cuenta o subcuenta del periodo que se entrega
    como parte de la contabilidad electrónica.

    :ivar cuenta: Nodo obligatorio para expresar los movimientos del
        periodo de cada uno de los auxiliares de la cuenta y/o
        subcuenta.
    :ivar version: Atributo requerido para expresar la versión del
        formato.
    :ivar rfc: Atributo requerido para expresar el RFC del contribuyente
        que envía los datos.
    :ivar mes: Atributo requerido para expresar el mes en que inicia la
        vigencia del auxiliar de la cuenta o subcuenta.
    :ivar anio: Atributo requerido para expresar el año al que inicia la
        vigencia del auxiliar de la cuenta o subcuenta.
    :ivar tipo_solicitud: Atributo requerido para expresar el tipo de
        envío del auxiliar de la cuenta o subcuenta ( AF - Acto de
        Fiscalización; FC - Fiscalización Compulsa; DE - Devolución; CO
        - Compensación )
    :ivar num_orden: Atributo opcional para expresar el número de orden
        asignado al acto de fiscalización al que hace referencia la
        solicitud del auxiliar de la cuenta o subcuenta. Requerido para
        tipo de solicitud = AF y FC. Se convierte en requerido cuando se
        cuente con la información.
    :ivar num_tramite: Atributo opcional para expresar el número de
        trámite asignado a la solicitud de devolución o compensación al
        que hace referencia el auxiliar de la cuenta o subcuenta.
        Requerido para tipo de solicitud  = DE  o CO. Se convierte en
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
        namespace = "http://www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas"
        namespace_prefix = "AuxiliarCtas"
        schema_location = "http://www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarCtas/AuxiliarCtas_1_3.xsd"

    cuenta: List["AuxiliarCtas.Cuenta"] = field(
        default_factory=list,
        metadata={
            "name": "Cuenta",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    version: str = field(
        init=False,
        default="1.3",
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
    mes: Optional[str] = field(
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
    tipo_solicitud: Optional[str] = field(
        default=None,
        metadata={
            "name": "TipoSolicitud",
            "type": "Attribute",
            "required": True,
            "pattern": r"AF|FC|DE|CO",
        }
    )
    num_orden: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumOrden",
            "type": "Attribute",
            "length": 13,
            "pattern": r"[A-Z]{3}[0-9]{7}(/)[0-9]{2}",
        }
    )
    num_tramite: Optional[str] = field(
        default=None,
        metadata={
            "name": "NumTramite",
            "type": "Attribute",
            "length": 14,
            "pattern": r"[A-Z]{2}[0-9]{12}",
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
    class Cuenta:
        """
        :ivar detalle_aux: Nodo obligatorio para expresar el detalle de
            los movimientos del periodo de cada uno de los auxiliares
        :ivar num_cta: Atributo requerido para expresar la clave con que
            se distingue  la cuenta o subcuenta que se afecta por la
            transacción que integra el auxiliar.
        :ivar des_cta: Atributo requerido para expresar el concepto de
            la cuenta o subcuenta que se afecta por la transacción que
            integra el auxiliar.
        :ivar saldo_ini: Atributo requerido para expresar el monto del
            saldo inicial de la cuenta o subcuenta del periodo del
            auxiliar. En caso de no existir dato, colocar cero (0)
        :ivar saldo_fin: Atributo requerido para expresar el monto del
            saldo final de la cuenta o subcuenta del periodo del
            auxiliar. En caso de no existir dato, colocar cero (0)
        """
        detalle_aux: List["AuxiliarCtas.Cuenta.DetalleAux"] = field(
            default_factory=list,
            metadata={
                "name": "DetalleAux",
                "type": "Element",
                "min_occurs": 1,
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
        des_cta: Optional[str] = field(
            default=None,
            metadata={
                "name": "DesCta",
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
                "min_inclusive": Decimal("-9999999999999999999999.99"),
                "max_inclusive": Decimal("9999999999999999999999.99"),
                "fraction_digits": 2,
            }
        )
        saldo_fin: Optional[Decimal] = field(
            default=None,
            metadata={
                "name": "SaldoFin",
                "type": "Attribute",
                "required": True,
                "min_inclusive": Decimal("-9999999999999999999999.99"),
                "max_inclusive": Decimal("9999999999999999999999.99"),
                "fraction_digits": 2,
            }
        )

        @dataclass
        class DetalleAux:
            """
            :ivar fecha: Atributo requerido para expresar la fecha de
                registro de la transacción que afecta la cuenta o
                subcuenta que integra el auxiliar.
            :ivar num_un_iden_pol: Atributo requerido para expresar el
                número único de identificación de la póliza. El campo
                deberá contener la clave o nombre utilizado por el
                contribuyente para diferenciar, el tipo de póliza y el
                número correspondiente. En un mes ordinario no debe
                repetirse un mismo número de póliza con la clave o
                nombre asignado por el contribuyente.
            :ivar concepto: Atributo requerido para expresar el concepto
                de la transacción  que integra el auxiliar.
            :ivar debe: Atributo requerido para expresar el monto del
                cargo de la cuenta o subcuenta de la transacción que
                integra el auxiliar. En caso de no existir dato, colocar
                cero (0)
            :ivar haber: Atributo requerido para expresar el monto del
                abono de la cuenta o subcuenta de la transacción que
                integra el auxiliar. En caso de no existir dato, colocar
                cero (0)
            """
            fecha: Optional[XmlDate] = field(
                default=None,
                metadata={
                    "name": "Fecha",
                    "type": "Attribute",
                    "required": True,
                }
            )
            num_un_iden_pol: Optional[str] = field(
                default=None,
                metadata={
                    "name": "NumUnIdenPol",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 50,
                }
            )
            concepto: Optional[str] = field(
                default=None,
                metadata={
                    "name": "Concepto",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 200,
                }
            )
            debe: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Debe",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": Decimal("-9999999999999999999999.99"),
                    "max_inclusive": Decimal("9999999999999999999999.99"),
                    "fraction_digits": 2,
                }
            )
            haber: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "Haber",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": Decimal("-9999999999999999999999.99"),
                    "max_inclusive": Decimal("9999999999999999999999.99"),
                    "fraction_digits": 2,
                }
            )
