public class Edukasi2 {

    public String idEdukasi;
    public String judul;
    public String isiPesan;
    public String tanggalKirim;
    public String idAdmin;
    public String idMasyarakat;

    public void showEdukasi() {
        System.out.println("ID Edukasi      : " + idEdukasi);
        System.out.println("Judul           : " + judul);
        System.out.println("Isi Pesan       : " + isiPesan);
        System.out.println("Tanggal Kirim   : " + tanggalKirim);
        System.out.println("ID Admin        : " + idAdmin);
        System.out.println("ID Masyarakat   : " + idMasyarakat);
    }

    public static void main(String[] args) {

        Edukasi2 edukasi1 = new Edukasi2();

        edukasi1.idEdukasi = "234543243";
        edukasi1.judul = "Sampah yang menggunung";
        edukasi1.isiPesan = "Buanglah sampah pada tempatnya";
        edukasi1.tanggalKirim = "19-02-2026";
        edukasi1.idAdmin = "ADM01";
        edukasi1.idMasyarakat = "MSY01";

        edukasi1.showEdukasi();
    }
}
