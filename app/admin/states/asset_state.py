import reflex as rx
from pathlib import Path
from reflex import UploadFile


class AssetState(rx.State):
    uploaded_files: list[str] = []
    is_loading: bool = False

    @rx.event(background=True)
    async def handle_upload(self, files: list[UploadFile]):
        if not files:
            yield rx.toast("No files selected")
            return
        async with self:
            self.is_loading = True
        yield
        for file in files:
            upload_data = await file.read()
            upload_path = (
                Path(rx.get_upload_dir()) / file.filename
            )
            with upload_path.open("wb") as f:
                f.write(upload_data)
            async with self:
                if file.filename not in self.uploaded_files:
                    self.uploaded_files.append(
                        file.filename
                    )
        async with self:
            self.is_loading = False
        yield rx.toast(f"Uploaded {len(files)} file(s)")

    def load_assets(self):
        upload_dir = Path(rx.get_upload_dir())
        if upload_dir.exists():
            self.uploaded_files = [
                f.name
                for f in upload_dir.iterdir()
                if f.is_file()
                and (not f.name.startswith("."))
            ]