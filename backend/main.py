# main.py
from rsa_core import generate_keypair, sign, verify
from utils import hash_document

def main():
    print("=== BACKEND DIGITAL SIGNATURE (RSA & SHA-256) ===")
    
    # 1. GENERATE KEY
    print("\n[1] Generating Keys...")
    # Menggunakan prima yang sedikit lebih besar agar muat menampung nilai hash integer SHA-256
    # Catatan: Untuk tugas lab, nilai prima ini sudah cukup mendemonstrasikan algoritma.
    p = 32416190071
    q = 32416190017
    public_key, private_key = generate_keypair(p, q)
    print(f"Public Key (e, n): {public_key}")
    print(f"Private Key (d, n): {private_key}")
    
    # Simulasi File PDF / TXT yang diupload oleh Frontend
    document_content = b"Ini adalah isi dokumen rahasia tugas besar mahasiswa IT."
    print(f"\nIsi Dokumen: {document_content.decode('utf-8')}")
    
    # 2. HASH DOKUMEN
    document_hash = hash_document(document_content)
    print(f"[2] Hash Dokumen (SHA-256): {document_hash}")
    
    # 3. DIGITAL SIGNING
    print("\n[3] Melakukan Digital Signing...")
    signature = sign(private_key, document_hash)
    print(f"Digital Signature Berhasil Dibuat: {signature}")
    
    # 4. VERIFIKASI (Kondisi 1: Dokumen Asli / Valid)
    print("\n[4] Pengujian Verifikasi (Dokumen Asli):")
    is_valid = verify(public_key, signature, document_hash)
    print(f"Status Verifikasi: {'VALID' if is_valid else 'TIDAK VALID'}")
    
    # 5. VERIFIKASI (Kondisi 2: Dokumen Diubah / Di-tamper)
    print("\n[5] Pengujian Verifikasi (Dokumen Telah Dimodifikasi):")
    tampered_content = b"Ini adalah isi dokumen rahasia tugas besar mahasiswa IT. (disisipi teks palsu)"
    tampered_hash = hash_document(tampered_content)
    is_valid_tampered = verify(public_key, signature, tampered_hash)
    print(f"Status Verifikasi Dokumen Palsu: {'VALID' if is_valid_tampered else 'TIDAK VALID'}")

if __name__ == "__main__":
    main()