Name:           purge_ram
Version:        1
Release:        0
Summary:        An Advance Bash Script for Purge RAM

Group:          Admins
BuildArch:      noarch
License:        GPL
URL:            https://github.com/darkwolf/purge_ram.git
Source0:        purge_ram-1.0.tar.gz

%description
Write some description about your package here

%prep
%setup -q
%build
%install
install -m 0755 -d $RPM_BUILD_ROOT/opt/purge_ram
install -m 0600 purge_ram.txt $RPM_BUILD_ROOT/opt/purge_ram/purge_ram.txt
install -m 0755 purge_ram.sh $RPM_BUILD_ROOT/opt/purge_ram/purge_ram.sh
install -m 0644 README.md $RPM_BUILD_ROOT/opt/purge_ram/README.md
install -m 0644 purge_ram.conf $RPM_BUILD_ROOT/opt/purge_ram/purge_ram.conf

%files
/opt/purge_ram
/opt/purge_ram/purge_ram.txt
/opt/purge_ram/purge_ram.sh
/opt/purge_ram/README.md
/opt/purge_ram/purge_ram.conf

%changelog
* Tue Oct 24 2021 DarkWolf  1.0.0
  - Initial rpm release
