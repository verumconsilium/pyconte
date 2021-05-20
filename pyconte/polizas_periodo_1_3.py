from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo"

@dataclass
class Polizas:
    """
    Estándar de pólizas del periodo que se entrega como parte de la
    contabilidad electrónica.

    :ivar poliza: Nodo obligatorio para relacionar el detalle de cada
        transacción dentro de la póliza.
    :ivar version: Atributo requerido para expresar la versión del
        formato.
    :ivar rfc: Atributo requerido para expresar el RFC del contribuyente
        que envía los datos
    :ivar mes: Atributo requerido para expresar el mes al que
        corresponde la póliza
    :ivar anio: Atributo requerido para expresar el año al que
        corresponde la póliza
    :ivar tipo_solicitud: Atributo requerido para expresar el tipo de
        solicitud de la póliza ( AF - Acto de Fiscalización; FC -
        Fiscalización Compulsa; DE - Devolución; CO - Compensación )
    :ivar num_orden: Atributo opcional para expresar el número de orden
        asignado al acto de fiscalización al que hace referencia la
        solicitud de la póliza. Requerido para tipo de solicitud = AF y
        FC. Se convierte en requerido cuando se cuente con la
        información.
    :ivar num_tramite: Atributo opcional para expresar el número de
        trámite asignado a la solicitud de devolución o compensación al
        que hace referencia la solicitud de la póliza. Requerido para
        tipo de solicitud  = DE  o CO. Se convierte en requerido cuando
        se cuente con la información.
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
        namespace = "http://www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo"
        namespace_prefix = "PLZ"
        schema_location = "http://www.sat.gob.mx/esquemas/ContabilidadE/1_3/PolizasPeriodo/PolizasPeriodo_1_3.xsd"

    poliza: List["Polizas.Poliza"] = field(
        default_factory=list,
        metadata={
            "name": "Poliza",
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
            "white_space": "collapse",
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
    class Poliza:
        """
        :ivar transaccion: Nodo obligatorio para relacionar el detalle
            de cada transacción dentro de la póliza
        :ivar num_un_iden_pol: Atributo requerido para expresar el
            número único de identificación de la póliza. El campo deberá
            contener la clave o nombre utilizado por el contribuyente
            para diferenciar, el tipo de póliza y el número
            correspondiente. En un mes ordinario no debe repetirse un
            mismo número de póliza con la clave o nombre asignado por el
            contribuyente.
        :ivar fecha: Atributo requerido para expresar la fecha de
            registro de la póliza
        :ivar concepto: Atributo requerido para expresar el concepto de
            la operación
        """
        transaccion: List["Polizas.Poliza.Transaccion"] = field(
            default_factory=list,
            metadata={
                "name": "Transaccion",
                "type": "Element",
                "min_occurs": 1,
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
        fecha: Optional[XmlDate] = field(
            default=None,
            metadata={
                "name": "Fecha",
                "type": "Attribute",
                "required": True,
            }
        )
        concepto: Optional[str] = field(
            default=None,
            metadata={
                "name": "Concepto",
                "type": "Attribute",
                "required": True,
                "min_length": 1,
                "max_length": 300,
            }
        )

        @dataclass
        class Transaccion:
            """
            :ivar comp_nal: Nodo opcional para relacionar el detalle de
                los comprobantes de origen nacional relacionados con la
                transacción. Se considera que se debe identificar, el
                soporte documental, tanto en la provisión, como en el
                pago y/o cobro de cada una de las cuentas y subcuentas
                que se vean afectadas.  Se convierte en requerido cuando
                se cuente con la información.
            :ivar comp_nal_otr: Nodo opcional para relacionar el detalle
                de los comprobantes de origen nacional relacionados con
                la transacción, diferente a CFDI, es decir, CFD y/o CBB.
                Se considera que se debe identificar, el soporte
                documental, tanto en la provisión, como en el pago y/o
                cobro de cada una de las cuentas y subcuentas que se
                vean afectadas. Se convierte en requerido cuando se
                cuente con la información.
            :ivar comp_ext: Nodo opcional para relacionar el detalle de
                los comprobantes de origen extranjero relacionados con
                la transacción.  Se considera que se debe identificar,
                el soporte documental, tanto en la provisión, como en el
                pago y/o cobro de cada una de las cuentas y subcuentas
                que se vean afectadas. Se convierte en requerido cuando
                se cuente con la información.
            :ivar cheque: Nodo opcional para relacionar el detalle de
                los cheques que integran la póliza. Se convierte en
                requerido cuando exista una salida o entrada de
                recursos, que involucre este método de pago o cobro de
                la obligación contraída por parte del contribuyente que
                envía los datos.
            :ivar transferencia: Nodo opcional para relacionar el
                detalle de las transferencias bancarias que integran la
                póliza. Se convierte en requerido cuando exista una
                salida o entrada de recursos que involucre este método
                de pago o cobro por parte del contribuyente que envía
                los datos. Además se convierte en requerido cuando se
                realicen transacciones, entre las cuentas propias del
                contribuyente.
            :ivar otr_metodo_pago: Nodo opcional para relacionar otros
                métodos de pago o cobro de la transacción. Se convierte
                en requerido cuando la transacción involucra un método
                de pago o cobro diverso a cheque y/o transferencia.
            :ivar num_cta: Atributo requerido para expresar la clave con
                que se distingue la cuenta o subcuenta que se afecta por
                la transacción.
            :ivar des_cta: Atributo requerido para expresar el nombre de
                la cuenta o subcuenta que se afecta por la transacción.
            :ivar concepto: Atributo requerido para expresar el concepto
                de la transacción
            :ivar debe: Atributo requerido para expresar el monto del
                cargo a la cuenta o subcuenta que se afecta en la
                transacción. En caso de no existir dato, colocar cero
                (0)
            :ivar haber: Atributo requerido para expresar el monto del
                abono a la cuenta o subcuenta que se afecta en la
                transacción. En caso de no existir dato, colocar cero
                (0)
            """
            comp_nal: List["Polizas.Poliza.Transaccion.CompNal"] = field(
                default_factory=list,
                metadata={
                    "name": "CompNal",
                    "type": "Element",
                }
            )
            comp_nal_otr: List["Polizas.Poliza.Transaccion.CompNalOtr"] = field(
                default_factory=list,
                metadata={
                    "name": "CompNalOtr",
                    "type": "Element",
                }
            )
            comp_ext: List["Polizas.Poliza.Transaccion.CompExt"] = field(
                default_factory=list,
                metadata={
                    "name": "CompExt",
                    "type": "Element",
                }
            )
            cheque: List["Polizas.Poliza.Transaccion.Cheque"] = field(
                default_factory=list,
                metadata={
                    "name": "Cheque",
                    "type": "Element",
                }
            )
            transferencia: List["Polizas.Poliza.Transaccion.Transferencia"] = field(
                default_factory=list,
                metadata={
                    "name": "Transferencia",
                    "type": "Element",
                }
            )
            otr_metodo_pago: List["Polizas.Poliza.Transaccion.OtrMetodoPago"] = field(
                default_factory=list,
                metadata={
                    "name": "OtrMetodoPago",
                    "type": "Element",
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
                    "min_exclusive": Decimal("-9999999999999999999999.99"),
                    "max_inclusive": Decimal("9999999999999999999999.99"),
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
                    "min_exclusive": Decimal("-9999999999999999999999.99"),
                    "max_inclusive": Decimal("9999999999999999999999.99"),
                    "fraction_digits": 2,
                    "white_space": "collapse",
                }
            )

            @dataclass
            class CompNal:
                """
                :ivar uuid_cfdi: Atributo requerido para expresar la
                    clave UUID del CFDI soporte de la operación. (36
                    caracteres)
                :ivar rfc: Atributo requerido para expresar el RFC
                    relacionado con el movimiento o transacción. El RFC
                    al que se hace referencia, es el distinto del
                    contribuyente que envía los datos, es decir, el RFC
                    del tercero vinculado.
                :ivar monto_total: Atributo requerido para expresar el
                    monto total del CFDI que soporte la transacción.
                    (Incluye IVA en su caso)
                :ivar moneda: Atributo opcional para expresar el tipo de
                    moneda utilizado en la transacción, de acuerdo al
                    catálogo publicado en la página de internet del SAT.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                :ivar tip_camb: Atributo opcional para expresar el tipo
                    de cambio utilizado de acuerdo al tipo de moneda.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                """
                uuid_cfdi: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "UUID_CFDI",
                        "type": "Attribute",
                        "required": True,
                        "length": 36,
                        "white_space": "collapse",
                        "pattern": r"[a-f0-9A-F]{8}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{4}-[a-f0-9A-F]{12}",
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
                monto_total: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "MontoTotal",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": Decimal("-9999999999999999999999.99"),
                        "max_inclusive": Decimal("9999999999999999999999.99"),
                        "fraction_digits": 2,
                        "white_space": "collapse",
                    }
                )
                moneda: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Moneda",
                        "type": "Attribute",
                    }
                )
                tip_camb: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "TipCamb",
                        "type": "Attribute",
                        "min_inclusive": Decimal("0"),
                        "total_digits": 19,
                        "fraction_digits": 5,
                    }
                )

            @dataclass
            class CompNalOtr:
                """
                :ivar cfd_cbb_serie: Atributo opcional para expresar la
                    serie del comprobante CFD_CBB que soporte la
                    transacción.
                :ivar cfd_cbb_num_fol: Atributo requerido para expresar
                    el número de folio del comprobante CFD_CBB que
                    soporte la transacción.
                :ivar rfc: Atributo requerido para expresar el RFC
                    relacionado con el movimiento o transacción. El RFC
                    al que se hace referencia, es el distinto del
                    contribuyente que envía los datos, es decir, el RFC
                    del tercero vinculado.
                :ivar monto_total: Atributo requerido para expresar el
                    monto total del CFD y/o CBB que soporte la
                    transacción. (Incluye IVA en su caso)
                :ivar moneda: Atributo opcional para expresar el tipo de
                    moneda utilizado en la transacción, de acuerdo al
                    catálogo publicado en la página de internet del SAT.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                :ivar tip_camb: Atributo opcional para expresar el tipo
                    de cambio utilizado de acuerdo al tipo de moneda.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                """
                cfd_cbb_serie: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CFD_CBB_Serie",
                        "type": "Attribute",
                        "min_length": 1,
                        "max_length": 10,
                        "pattern": r"[A-Z]+",
                    }
                )
                cfd_cbb_num_fol: Optional[int] = field(
                    default=None,
                    metadata={
                        "name": "CFD_CBB_NumFol",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 1,
                        "total_digits": 20,
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
                monto_total: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "MontoTotal",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": Decimal("-9999999999999999999999.99"),
                        "max_inclusive": Decimal("9999999999999999999999.99"),
                        "fraction_digits": 2,
                        "white_space": "collapse",
                    }
                )
                moneda: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Moneda",
                        "type": "Attribute",
                    }
                )
                tip_camb: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "TipCamb",
                        "type": "Attribute",
                        "min_inclusive": Decimal("0"),
                        "total_digits": 19,
                        "fraction_digits": 5,
                    }
                )

            @dataclass
            class CompExt:
                """
                :ivar num_fact_ext: Atributo requerido para expresar la
                    clave numérico o alfanumérico del comprobante de
                    origen extranjero que soporte la operación
                :ivar tax_id: Atributo opcional que sirve para expresar
                    el Identificador del contribuyente extranjero. Se
                    convierte en requerido cuando se cuente con la
                    información
                :ivar monto_total: Atributo requerido para expresar el
                    monto total del comprobante de origen extranjero que
                    soporte la operación.
                :ivar moneda: Atributo opcional para expresar el tipo de
                    moneda utilizado en la transacción, de acuerdo al
                    catálogo publicado en la página de internet del SAT.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                :ivar tip_camb: Atributo opcional para expresar el tipo
                    de cambio utilizado de acuerdo al tipo de moneda.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                """
                num_fact_ext: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "NumFactExt",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 36,
                        "white_space": "collapse",
                    }
                )
                tax_id: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "TaxID",
                        "type": "Attribute",
                        "min_length": 1,
                        "max_length": 30,
                        "white_space": "collapse",
                    }
                )
                monto_total: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "MontoTotal",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": Decimal("-9999999999999999999999.99"),
                        "max_inclusive": Decimal("9999999999999999999999.99"),
                        "fraction_digits": 2,
                        "white_space": "collapse",
                    }
                )
                moneda: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Moneda",
                        "type": "Attribute",
                    }
                )
                tip_camb: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "TipCamb",
                        "type": "Attribute",
                        "min_inclusive": Decimal("0"),
                        "total_digits": 19,
                        "fraction_digits": 5,
                    }
                )

            @dataclass
            class Cheque:
                """
                :ivar num: Atributo requerido para expresar el número
                    del cheque emitido
                :ivar ban_emis_nal: Atributo requerido, para expresar el
                    Banco nacional emisor del cheque, de acuerdo al
                    catálogo publicado en la página de internet del SAT.
                    Se consideran banco nacional aquellos bancos de
                    residencia nacional, indistintamente, si el tipo de
                    moneda es nacional o extranjero.
                :ivar ban_emis_ext: Atributo opcional para expresar el
                    nombre completo del Banco extranjero emisor del
                    cheque. Se convierte en requerido cuando se cuente
                    con la información.
                :ivar cta_ori: Atributo requerido para expresar el
                    número de cuenta bancaria del origen de los
                    recursos.
                :ivar fecha: Atributo requerido, es la fecha del cheque
                :ivar benef: Atributo requerido, nombre del beneficiario
                    del cheque
                :ivar rfc: Atributo requerido para expresar el RFC
                    relacionado con el movimiento. El RFC al que se hace
                    referencia, es el distinto del contribuyente que
                    envía los datos, es decir, el RFC del tercero
                    vinculado.
                :ivar monto: Atributo requerido, es el monto del cheque
                    emitido
                :ivar moneda: Atributo opcional para expresar el tipo de
                    moneda utilizado en la transacción, de acuerdo al
                    catálogo publicado en la página de internet del SAT.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                :ivar tip_camb: Atributo opcional para expresar el tipo
                    de cambio utilizado de acuerdo al tipo de moneda.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                """
                num: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Num",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 20,
                    }
                )
                ban_emis_nal: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "BanEmisNal",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                ban_emis_ext: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "BanEmisExt",
                        "type": "Attribute",
                        "max_length": 150,
                    }
                )
                cta_ori: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CtaOri",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 50,
                    }
                )
                fecha: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "name": "Fecha",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                benef: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Benef",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 300,
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
                monto: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "Monto",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": Decimal("-9999999999999999999999.99"),
                        "max_inclusive": Decimal("9999999999999999999999.99"),
                        "fraction_digits": 2,
                        "white_space": "collapse",
                    }
                )
                moneda: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Moneda",
                        "type": "Attribute",
                    }
                )
                tip_camb: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "TipCamb",
                        "type": "Attribute",
                        "min_inclusive": Decimal("0"),
                        "total_digits": 19,
                        "fraction_digits": 5,
                    }
                )

            @dataclass
            class Transferencia:
                """
                :ivar cta_ori: Atributo opcional para expresar el número
                    de cuenta de origen desde la cual se transfieren los
                    recursos. Se convierte en requerido cuando se cuente
                    con la información.
                :ivar banco_ori_nal: Atributo requerido, para expresar
                    el Banco de la cuenta origen de la transferencia, de
                    acuerdo al catálogo publicado en la página de
                    internet del SAT. Se considera banco nacional
                    aquellos bancos de residencia nacional,
                    indistintamente, si el tipo de moneda es nacional o
                    extranjero.
                :ivar banco_ori_ext: Atributo opcional para expresar el
                    nombre completo del banco origen extranjero. Se
                    convierte en requerido cuando se cuente con la
                    información.
                :ivar cta_dest: Atributo requerido para expresar el
                    número de cuenta destino, la cual se transfieren los
                    recursos.
                :ivar banco_dest_nal: Atributo requerido, para expresar
                    el Banco de la cuenta destino de la transferencia,
                    de acuerdo al catálogo publicado en la página de
                    internet del SAT. Se considera banco nacional
                    aquellos bancos de residencia nacional,
                    indistintamente, si el tipo de moneda es nacional o
                    extranjero.
                :ivar banco_dest_ext: Atributo opcional para expresar el
                    nombre completo del banco destino extranjero. Se
                    convierte en requerido cuando se cuente con la
                    información.
                :ivar fecha: Atributo requerido, es la fecha de la
                    transferencia
                :ivar benef: Atributo requerido, nombre del beneficiario
                    de la transferencia.
                :ivar rfc: Atributo requerido para expresar el RFC
                    relacionado con el movimiento. El RFC al que se hace
                    referencia, es el distinto del contribuyente que
                    envía los datos, es decir, el RFC del tercero
                    vinculado.
                :ivar monto: Atributo requerido, es el monto transferido
                :ivar moneda: Atributo opcional para expresar el tipo de
                    moneda utilizado en la transacción, de acuerdo al
                    catálogo publicado en la página de internet del SAT.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                :ivar tip_camb: Atributo opcional para expresar el tipo
                    de cambio utilizado de acuerdo al tipo de moneda.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                """
                cta_ori: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CtaOri",
                        "type": "Attribute",
                        "min_length": 1,
                        "max_length": 50,
                    }
                )
                banco_ori_nal: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "BancoOriNal",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                banco_ori_ext: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "BancoOriExt",
                        "type": "Attribute",
                        "max_length": 150,
                    }
                )
                cta_dest: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "CtaDest",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 50,
                    }
                )
                banco_dest_nal: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "BancoDestNal",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                banco_dest_ext: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "BancoDestExt",
                        "type": "Attribute",
                        "max_length": 150,
                    }
                )
                fecha: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "name": "Fecha",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                benef: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Benef",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 300,
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
                monto: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "Monto",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": Decimal("-9999999999999999999999.99"),
                        "max_inclusive": Decimal("9999999999999999999999.99"),
                        "fraction_digits": 2,
                        "white_space": "collapse",
                    }
                )
                moneda: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Moneda",
                        "type": "Attribute",
                    }
                )
                tip_camb: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "TipCamb",
                        "type": "Attribute",
                        "min_inclusive": Decimal("0"),
                        "total_digits": 19,
                        "fraction_digits": 5,
                    }
                )

            @dataclass
            class OtrMetodoPago:
                """
                :ivar met_pago_pol: Atributo requerido para expresar el
                    método de pago de la operación, de acuerdo al
                    catálogo publicado en la página de internet del SAT.
                :ivar fecha: Atributo requerido, es la fecha de la
                    transacción de otros métodos de pago.
                :ivar benef: Atributo requerido, nombre de la persona o
                    contribuyente a la cual se realiza éstos métodos de
                    pago.
                :ivar rfc: Atributo requerido para expresar el RFC
                    relacionado con la transacción. El RFC al que se
                    hace referencia, es el distinto del contribuyente
                    que envía los datos, es decir, el RFC del tercero
                    vinculado.
                :ivar monto: Atributo requerido para expresar el monto
                    del método de pago soporte de la transacción.
                :ivar moneda: Atributo opcional para expresar el tipo de
                    moneda utilizado en la transacción, de acuerdo al
                    catálogo publicado en la página de internet del SAT.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                :ivar tip_camb: Atributo opcional para expresar el tipo
                    de cambio utilizado de acuerdo al tipo de moneda.
                    Este dato sólo se utiliza en el caso de que el tipo
                    de moneda, sea diferente a la moneda nacional
                    (peso). Se convierte en requerido cuando se cuente
                    con la información.
                """
                met_pago_pol: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "MetPagoPol",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                fecha: Optional[XmlDate] = field(
                    default=None,
                    metadata={
                        "name": "Fecha",
                        "type": "Attribute",
                        "required": True,
                    }
                )
                benef: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Benef",
                        "type": "Attribute",
                        "required": True,
                        "min_length": 1,
                        "max_length": 300,
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
                monto: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "Monto",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": Decimal("-9999999999999999999999.99"),
                        "max_inclusive": Decimal("9999999999999999999999.99"),
                        "fraction_digits": 2,
                        "white_space": "collapse",
                    }
                )
                moneda: Optional[str] = field(
                    default=None,
                    metadata={
                        "name": "Moneda",
                        "type": "Attribute",
                    }
                )
                tip_camb: Optional[Decimal] = field(
                    default=None,
                    metadata={
                        "name": "TipCamb",
                        "type": "Attribute",
                        "min_inclusive": Decimal("0"),
                        "total_digits": 19,
                        "fraction_digits": 5,
                    }
                )
