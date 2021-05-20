from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios"

@dataclass
class RepAuxFol:
    """
    Estándar de reporte auxiliar de folios de los comprobantes fiscales de las
    pólizas que se entrega como parte de las pólizas de la contabilidad
    electrónica.

    :ivar det_aux_fol: Nodo opcional para expresar el detalle de los
        folios de los comprobantes fiscales que integran la póliza.
    :ivar version: Atributo requerido para expresar la versión del
        formato.
    :ivar rfc: Atributo requerido para expresar el RFC del contribuyente
        que envía los datos
    :ivar mes: Atributo requerido para expresar el mes en que inicia la
        vigencia del reporte auxiliar de los folios de los comprobantes
        fiscales de las pólizas.
    :ivar anio: Atributo requerido para expresar el año al que inicia la
        vigencia del reporte auxiliar de los folios de los comprobantes
        fiscales de las pólizas.
    :ivar tipo_solicitud: Atributo requerido para expresar el tipo de
        solicitud del reporte auxiliar de los folios de los comprobantes
        fiscales de las pólizas. ( AF - Acto de Fiscalización; FC -
        Fiscalización Compulsa; DE - Devolución; CO - Compensación )
    :ivar num_orden: Atributo opcional para expresar el número de orden
        asignado al acto de fiscalización al que hace referencia el
        reporte auxiliar de los folios de los comprobantes fiscales de
        las pólizas. Requerido para tipo de solicitud = AF y FC. Se
        convierte en requerido cuando se cuente con la información.
    :ivar num_tramite: Atributo opcional para expresar el número de
        trámite asignado a la solicitud de devolución o compensación al
        que hace referencia el reporte auxiliar de los folios de los
        comprobantes fiscales de las pólizas. Requerido para tipo de
        solicitud  = DE  o CO. Se convierte en requerido cuando se
        cuente con la información.
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
        namespace = "http://www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios"
        namespace_prefix = "RepAux"
        schema_location = "http://www.sat.gob.mx/esquemas/ContabilidadE/1_3/AuxiliarFolios/AuxiliarFolios_1_3.xsd"

    det_aux_fol: List["RepAuxFol.DetAuxFol"] = field(
        default_factory=list,
        metadata={
            "name": "DetAuxFol",
            "type": "Element",
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
            "pattern": r"AF|DE|CO|FC",
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
    class DetAuxFol:
        """
        :ivar compr_nal: Nodo opcional para relacionar el detalle de los
            comprobantes de origen nacional relacionados con la
            transacción. Se considera que se debe identificar, el
            soporte documental, tanto en la provisión, como en el pago
            y/o cobro de cada una de las cuentas y subcuentas que se
            vean afectadas.  Se convierte en requerido cuando se cuente
            con la información.
        :ivar compr_nal_otr: Nodo opcional para relacionar el detalle de
            los comprobantes de origen nacional relacionados con la
            transacción, diferente a CFDI, es decir, CFD y/o CBB. Se
            considera que se debe identificar, el soporte documental,
            tanto en la provisión, como en el pago y/o cobro de cada una
            de las cuentas y subcuentas que se vean afectadas. Se
            convierte en requerido cuando se cuente con la información.
        :ivar compr_ext: Nodo opcional para relacionar el detalle de los
            comprobantes de origen extranjero relacionados con la
            transacción. Se considera que se debe identificar, el
            soporte documental, tanto en la provisión, como en el pago
            y/o cobro de cada una de las cuentas y subcuentas que se
            vean afectadas. Se convierte en requerido cuando se cuente
            con la información.
        :ivar num_un_iden_pol: Atributo requerido para expresar el
            número único de identificación de la póliza. El campo deberá
            contener la clave o nombre utilizado por el contribuyente
            para diferenciar, el tipo de póliza y el número
            correspondiente. En un mes ordinario no debe repetirse un
            mismo número de póliza con la clave o nombre asignado por el
            contribuyente.
        :ivar fecha: Atributo requerido para expresar la fecha de
            registro de la póliza.
        """
        compr_nal: List["RepAuxFol.DetAuxFol.ComprNal"] = field(
            default_factory=list,
            metadata={
                "name": "ComprNal",
                "type": "Element",
            }
        )
        compr_nal_otr: List["RepAuxFol.DetAuxFol.ComprNalOtr"] = field(
            default_factory=list,
            metadata={
                "name": "ComprNalOtr",
                "type": "Element",
            }
        )
        compr_ext: List["RepAuxFol.DetAuxFol.ComprExt"] = field(
            default_factory=list,
            metadata={
                "name": "ComprExt",
                "type": "Element",
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

        @dataclass
        class ComprNal:
            """
            :ivar uuid_cfdi: Atributo requerido para expresar la clave
                UUID del CFDI soporte de la operación. (36 caracteres)
            :ivar monto_total: Atributo requerido para expresar el
                monto  total del CFDI que soporte la operación  (Incluye
                IVA en su caso)
            :ivar rfc: Atributo requerido para expresar el RFC
                relacionado con la operación. El RFC al que se hace
                referencia, es el distinto del contribuyente que envía
                los datos, es decir, el RFC del tercero vinculado.
            :ivar met_pago_aux: Atributo opcional para expresar el
                método de pago de la operación, de acuerdo al catálogo
                publicado en la página de internet del SAT. Se convierte
                en requerido cuando se cuente con la información.
            :ivar moneda: Atributo opcional para expresar el tipo de
                moneda utilizado en la transacción, de acuerdo al
                catálogo publicado en la página de internet del SAT.
                Este dato sólo se utiliza en el caso de que el tipo de
                moneda, sea diferente a la moneda nacional (peso). Se
                convierte en requerido cuando se cuente con la
                información.
            :ivar tip_camb: Atributo opcional para expresar el tipo de
                cambio utilizado de acuerdo al tipo de moneda. Este dato
                sólo se utiliza en el caso de que el tipo de moneda, sea
                diferente a la moneda nacional (peso). Se convierte en
                requerido cuando se cuente con la información.
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
            monto_total: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "MontoTotal",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": Decimal("-9999999999999999999999.99"),
                    "max_inclusive": Decimal("9999999999999999999999.99"),
                    "fraction_digits": 2,
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
            met_pago_aux: Optional[str] = field(
                default=None,
                metadata={
                    "name": "MetPagoAux",
                    "type": "Attribute",
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
        class ComprNalOtr:
            """
            :ivar cfd_cbb_serie: Atributo opcional para expresar la
                serie del comprobante CFD_CBB que soporte la operación.
            :ivar cfd_cbb_num_fol: Atributo requerido para expresar el
                número de folio del comprobante CFD_CBB que soporte la
                operación.
            :ivar monto_total: Atributo requerido para expresar el monto
                total del CFD y/o CBB que soporte la operación. (Incluye
                IVA en su caso)
            :ivar rfc: Atributo requerido para expresar el RFC
                relacionado con la operación. El RFC al que se hace
                referencia, es el distinto del contribuyente que envía
                los datos, es decir, el RFC del tercero vinculado.
            :ivar met_pago_aux: Atributo opcional para expresar el
                método de pago de la operación, de acuerdo al catálogo
                publicado en la página de internet del SAT. Se convierte
                en requerido cuando se cuente con la información.
            :ivar moneda: Atributo opcional para expresar el tipo de
                moneda utilizado en la transacción, de acuerdo al
                catálogo publicado en la página de internet del SAT.
                Este dato sólo se utiliza en el caso de que el tipo de
                moneda, sea diferente a la moneda nacional (peso). Se
                convierte en requerido cuando se cuente con la
                información.
            :ivar tip_camb: Atributo opcional para expresar el tipo de
                cambio utilizado de acuerdo al tipo de moneda. Este dato
                sólo se utiliza en el caso de que el tipo de moneda, sea
                diferente a la moneda nacional (peso). Se convierte en
                requerido cuando se cuente con la información.
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
            monto_total: Optional[Decimal] = field(
                default=None,
                metadata={
                    "name": "MontoTotal",
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": Decimal("-9999999999999999999999.99"),
                    "max_inclusive": Decimal("9999999999999999999999.99"),
                    "fraction_digits": 2,
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
            met_pago_aux: Optional[str] = field(
                default=None,
                metadata={
                    "name": "MetPagoAux",
                    "type": "Attribute",
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
        class ComprExt:
            """
            :ivar num_fact_ext: Atributo requerido para expresar la
                clave numérico o alfanumérico del comprobante de origen
                extranjero que soporte la operación
            :ivar tax_id: Atributo opcional que sirve para expresar el
                Identificador del contribuyente extranjero. Se convierte
                en requerido cuando se cuente con la información
            :ivar monto_total: Atributo requerido para expresar el monto
                total del comprobante de origen extranjero que soporte
                la operación.
            :ivar met_pago_aux: Atributo opcional para expresar el
                método de pago de la operación, de acuerdo al catálogo
                publicado en la página de internet del SAT. Se convierte
                en requerido cuando se cuente con la información.
            :ivar moneda: Atributo opcional para expresar el tipo de
                moneda utilizado en la transacción, de acuerdo al
                catálogo publicado en la página de internet del SAT.
                Este dato sólo se utiliza en el caso de que el tipo de
                moneda, sea diferente a la moneda nacional (peso). Se
                convierte en requerido cuando se cuente con la
                información.
            :ivar tip_camb: Atributo opcional para expresar el tipo de
                cambio utilizado de acuerdo al tipo de moneda. Este dato
                sólo se utiliza en el caso de que el tipo de moneda, sea
                diferente a la moneda nacional (peso). Se convierte en
                requerido cuando se cuente con la información.
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
                    "min_inclusive": Decimal("-9999999999999999999999.99"),
                    "max_inclusive": Decimal("9999999999999999999999.99"),
                    "fraction_digits": 2,
                }
            )
            met_pago_aux: Optional[str] = field(
                default=None,
                metadata={
                    "name": "MetPagoAux",
                    "type": "Attribute",
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
