from datetime import timedelta

from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.utils import timezone

from ...models import Log


# Fixtureをインポート後、データの日付を現在に合わせて修正'
class Command(BaseCommand):

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        # データ削除
        Log.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('data cleared'))
        # fixtureをインポート
        call_command('loaddata', 'dump.json')
        self.stdout.write(self.style.SUCCESS('data reloaded'))

        # ダミーデータの更新 現在時間～七日前のデータに直す
        logs = Log.objects.all().order_by('-created_at')
        for index, log in enumerate(logs):
            log.created_at = timezone.now().replace(minute=0, second=0, microsecond=0) - timedelta(hours=index)
            log.save()

        self.stdout.write(self.style.SUCCESS('data updated'))
