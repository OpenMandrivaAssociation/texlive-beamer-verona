%global tl_name beamer-verona
%global tl_revision 39180

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	A theme for the beamer class
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/beamer-verona
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-verona.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamer-verona.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the 'Verona' theme for the beamer class by Till
Tantau.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamer-verona
%dir %{_datadir}/texmf-dist/tex/latex/beamer-verona
%doc %{_datadir}/texmf-dist/doc/latex/beamer-verona/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamer-verona/beamer-verona-default.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer-verona/beamer-verona-default.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer-verona/beamer-verona-sidebar.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer-verona/beamer-verona-sidebar.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamer-verona/beamer-verona.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamer-verona/plato-aristotle.jpg
%{_datadir}/texmf-dist/tex/latex/beamer-verona/beamerthemeVerona.sty
