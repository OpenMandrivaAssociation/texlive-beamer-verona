Name:		texlive-beamer-verona
Version:	39180
Release:	1
Summary:	A theme for the beamer class
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-verona
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-verona.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-verona.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides the 'Verona' theme for the beamer class
by Till Tantau.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamer-verona
%doc %{_texmfdistdir}/doc/latex/beamer-verona

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
