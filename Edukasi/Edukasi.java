package Edukasi;

public class Edukasi {

    public String idEdukasi;
    public String judul;
    public String isiPesan;
    public String tanggalKirim;
    public String idAdmin;
    public String idMasyarakat;

    public static void main(String[] args) {

        Edukasi Edukasi1 = new Edukasi();
        Edukasi1.idEdukasi = "EDS08";
        Edukasi1.judul = "sampah yang menggunung";
        Edukasi1.isiPesan = "buanglah sampah pada tempatnya";
        Edukasi1.tanggalKirim = "02-10-2026";
        Edukasi1.idAdmin = "ADM93";
        Edukasi1.idMasyarakat = "M009";

        System.out.println("ID Edukasi      : " + Edukasi1.idEdukasi);
        System.out.println("Judul           : " + Edukasi1.judul);
        System.out.println("Isi Pesan       : " + Edukasi1.isiPesan);
        System.out.println("Tanggal Kirim   : " + Edukasi1.tanggalKirim);
        System.out.println("ID Admin        : " + Edukasi1.idAdmin);
        System.out.println("ID Masyarakat   : " + Edukasi1.idMasyarakat);
    }
}
