package Edukasi;

public class Edukasi {

    public String idEdukasi;
    public String judul;
    public String isiPesan;
    public String tanggalKirim;
    public String idAdmin;
    public String idMasyarakat;

    public static void main(String[] args) {

        Edukasi eds = new Edukasi();
        eds.idEdukasi = "23454321";
        eds.judul = "sampah yang menggunung";
        eds.isiPesan = "buanglah sampah pada tempatnya";
        eds.tanggalKirim = "02-10-2026";
        eds.idAdmin = "E093";
        eds.idMasyarakat = "0009";

        System.out.println("ID Edukasi : " + eds.idEdukasi);
        System.out.println("Judul : " + eds.judul);
        System.out.println("Isi Pesan : " + eds.isiPesan);
        System.out.println("Tanggal Kirim : " + eds.tanggalKirim);
        System.out.println("ID Admin : " + eds.idAdmin);
        System.out.println("ID Masyarakat : " + eds.idMasyarakat);
    }
}
